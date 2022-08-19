Problem statement

for this project we use entirely a conda environment
install pip files 
the commands is yellow are to be run with in the cli 


ensure terminals(cli) are in the same folder and the environment is activated

NOTE: a more detailed readme on each individual process has been included in each folder 
DATASET
we create an infrasrtucture for the state for the backend
we crate a bucket to store our dataset using terraform
we execute a python script, that gets data from kaggle, sort the data by years, divides the data into 4 and uploades it into our s3 bucket 

MODEL CHOOSING
we move to the choosing of model 
we download the data from our bucket using the s3fs python library 
we do some exploratory data analysis to see which features that influence the house prices 
we set up a bucket in the cloud to store our chosen model 

ORCHESTRATION
orchestration with prefect, model registry to choose best training mmodel and teting 
run pytnon 3 to train model
use sqlite3 as db

WEBSERVICE




MONITORING