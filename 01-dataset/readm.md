Firstly, we create a bucket manually in aws so that we can put the terraform-state there, so that it can be used as our backend  instead of having it locally,

then we use terraform as Iac tool, 
we use the terraform files in the terraform folder to create an s3 bucket where we will store our dataset

Using the files in the terrafom folder, the following commands we used 
  
terraform init -> which initializes the terrafom state
terraform plan -> which shows the planned configuration
terraform validate -> to ensure the configuration is valid
terraform apply -> to apply the configuration

################### terraform image 

After the S3 bucket named (mlops-project-dataset-deen) was created with terraform

split_dataset was written in jupyter notebook and converted to a ![python script](mlops-project/dataset/python_script)

data was downloaded to local using a python script, with a bash script(script.sh) embeded inside the the python script, the python script uses the bash script to download the file, after which it sorts the file by year and splits it into 4 equal dataset then stores them in the data folder, each of the datasets are stored are stored in periods, so we have them from period 01 to 04, -> in this context we are creating a scenerio where we are assuming that data comes in at the end of each period, after that, we wrote a "convert to parquet function, that converts the files from csv to parquet files and under the same function, it uploads the files to the s3 bucket we created using terraform.  


############### image of file in S3

to run  the python script
-ensure you have you valid keys from the kaggle website replaced with that which is in the script.sh file (if this isnt done, you get 401 error)
    export KAGGLE_USERNAME=yusufkaxxxxxxxxxxxxx
    export KAGGLE_KEY=f5779e2007b3e41b613xxxxxxxxxxxx

-> ensure that you have a valid S3 bucket location, which should be the same with the one we used the terraform to create
-> note that the aws cli has to be configured before you can run this command from the cli 
    -> instructions on how to authenticate your aws-cli can be found here
     ![aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)



# python split_dataset.py 
to run the python script, you run the above command in terminal

NOTE: that two files are downloaded when you run the python the script, 1 of which is only 98% complete and the other is 100% complete, we will only be focusing on the one which is 100% complete  

#dataset location
![kaggle dataset](https://www.kaggle.com/datasets/mssmartypants/paris-housing-price-prediction)

#more on boto3
![boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html)

to convert the notebook to a script we use the command below
# jupyter nbconvert --to script split_dataset.ipynb

