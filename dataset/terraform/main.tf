
# Make sure to create state bucket beforehand,was created manually
#this bucket is for storing our terraform state
terraform {
  required_version = ">= 1.0"
  backend "s3" {
    bucket  = "tf-state-mlops-project-backend"
    key     = "mlops_dataset.tfstate"
    region  = "eu-west-3"
    encrypt = true
  }
}

provider "aws" {
  region = var.aws_region
}
#this is the bucket where we store our dataset
resource "aws_s3_bucket" "s3_bucket_deen" {
  bucket        = var.bucket_name
  acl           = "private"
  force_destroy = true
}


output "name" {
  value = var.project_id
}

