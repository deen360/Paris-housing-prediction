
# Make sure to create state bucket beforehand,was created manually 
#our bucket terraform state is stored in the tf-state-mlops-project-backend" just like we did for the dataset
terraform {
  required_version = ">= 1.0"
  backend "s3" {
    bucket  = "tf-state-mlops-project-backend"
    key     = "mlops_infrastructure.tfstate"
    region  = "eu-west-3"
    encrypt = true
  }
}

provider "aws" {
  region = var.aws_region
}

#we are setting up abucket to store the model
resource "aws_s3_bucket" "s3_bucket_deen_1" {
  bucket        = var.bucket_name_1
  acl           = "private"
  force_destroy = true
}


