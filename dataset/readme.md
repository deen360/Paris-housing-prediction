first we create a bucket manually in aws so that we can put the terraform state there, before running the terraform iinit comand, so that our bucket can be on the cloud 

set up s3 BUCKET IN terraform 
terraform init 
terraform plan 
terraform apply

the bucket is for the dataset 

split_dataset was written in jupyter notebook and converted to a python script 

you can run the python script from your command line python3 split_dataset.py 
put your keys in the script.sh file
ensure you have the required libraries installed and aws-cli authenticated 
ensure you are in the same folder where the files are located 
check the pipfile to see other packages installed 

boto3 dcoumentation
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html


#to convert the notebook to a script
jupyter nbconvert --to script split_dataset.ipynb