Problem statement:
the global aim of this project is to develop an end to end machine learning operations, from sourcing of datatset, to experiment tracking, orchestration,deployment and monitoring of our models as well as following the best practices, the datatset chosen was based on the interest of helping people living in paris to be able to estimate the cost of house, in order make better decisons, as houses are quite expensive in the area 


final deployment available  on   [paris-prediction](https://paris-housing-prediction.herokuapp.com/)

conda enviroment was used for this project:
before we start the project, we create a conda environment installing all the dependencies 
	from conda base
	
	#we run the follwing command: 
		conda env create -f environment.yml  -> creates a conda environment with the enviroment.yml file
		conda activate project -> this activate the projects environment created in the enviroment.yml file
		make setup -> the runs the setup in the make file, installing all the dependencies to our new environment


NOTES:
	the commands in yellow are to be run with in the terminal/cli 
	ensure terminals are in the same folder and the environment is always activated
	 


DATASET  [kaggle dataset](https://www.kaggle.com/datasets/mssmartypants/paris-housing-price-prediction)
an infrastructure for the terraform-state for the backend 
a bucket to store our dataset is created using terraform
a python script is executed, which gets data from kaggle, sorts the data by years, divides the data into 4 periods and uploades them into s3 bucket created



MODEL CHOOSING
the choosing of model 
data is read directly from the s3 bucket using the boto3 python library 
exploratory data analysis are done to see which features  influences the house prices 
different algorithms are tried and the best model is chosen using model registry


ORCHESTRATION
orchestration with prefect and model registry to choose best training model as well as testing, 
we also automated the training of the model using prefect 2.0.3 (there might be a newer version)

WEBSERVICE
we test the predict.py file with test.py 
everyting is packaged into a container ready for deployment 


MONITORING
we use both the online monitoring with prometheus and grafana, using evidently ai 
we have a report generated with evidently which is available in evidently_report_example.html in the monitoring folder

FLASK-DEPLOYMENT
 here we run flask tests, to test the routes of the application to be deployed and to make sure all the error checks are avoided 
 the test are done using pytest, and files can be found in the flask folder in this deployment, we used mongodb clusters as database, so that any input from any user online will go state to our database (mongodb clusters).
 
 deployment is available  [paris-prediction](https://paris-housing-prediction.herokuapp.com/)



BEST PRACTICES
Makefile -> the make file includes the quality checks and the also the setup, which are both activated using 
	
	-> make setup 
		installation of requirements

	-> make quality checks (linting and formatting)
			black pylint sort 

![Screenshot from 2022-09-03 20-16-06](https://user-images.githubusercontent.com/74934494/188283333-90387c7c-d782-4cd1-81d2-32d93ebe4120.png)


