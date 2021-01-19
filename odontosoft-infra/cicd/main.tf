resource "aws_codebuild_project" "build-image" {
  name          = join("", ["CreateGoldenImage-", var.projectname])
  description   = join("", ["Build project to create the golden image for ", var.projectname])
  service_role  = aws_iam_role.codebuild-role.arn

  artifacts {
    type = "CODEPIPELINE"
  }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/standard:5.0"
    type                        = "LINUX_CONTAINER"
    image_pull_credentials_type = "SERVICE_ROLE"
 }
 source {
     type   = "CODEPIPELINE"
     buildspec = file("../buildspec.yml")
 }
}