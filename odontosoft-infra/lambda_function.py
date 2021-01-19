import boto3
import os
import logging

def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    cb_project_name = os.environ['codebuild_project_name']
    client_cb = boto3.client('codebuild')
    client_codepipeline = boto3.client('codepipeline')
    
    codepipeline_job_id = event["CodePipeline.job"]['id'] 
    image_name = event["CodePipeline.job"]['data']['actionConfiguration']['configuration']['UserParameters']
    
    logger.info("Image_name: " + image_name)
    environment_value = {
        "image": image_name,
        "computeType": "BUILD_GENERAL1_SMALL",
        "type": "LINUX_CONTAINER"
    }
    try:
        response_codebuild = client_cb.update_project(name = cb_project_name, environment = environment_value)
        logger.info(response_codebuild)
        response = client_codepipeline.put_job_success_result(jobId=codepipeline_job_id)
        logger.debug(response)
    except Exception as error:
        logger.exception(error)
        response = client_codepipeline.put_job_failure_result(
            jobId=codepipeline_job_id,
            failureDetails={
              'type': 'JobFailed',
              'message': f'{error.__class__.__name__}: {str(error)}'
            }
        )
        logger.debug(response)