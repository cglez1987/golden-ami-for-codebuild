terraform {
  backend "s3" {
    bucket = "goldenami-odontosoft-infra-cicd-terraform-state"
    encrypt = true
    key = "terraform.tfstate"
  }
}