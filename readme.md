DATASET
we create an infrasrtucture for the state for the backend
we crate a bucket to store our dataset using terraform
we execute a python script, that gets data from kaggle, sort the data by years, divides the data into 4 and uploades it into our s3 bucket 

MODEL CHOOSING
we move to the choosing of model 
we download the data from our bucket using the s3fs python library 
we do some exploratory data analysis to see which features that influence the house prices 
we set up a bucket in the cloud to store our chosen model 

orchestration with prefect, model registry to choose best training mmodel and teting 
run pytnon 3 to train model
use sqlite3 as db