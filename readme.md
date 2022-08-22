Problem statement:
the global aim of this project is to develop an end to end machine learning operations, from sourcing of datatset, to experiment tracking, orchestration,deployment and monitoring of our models as well as following the best practices, the datatset chosen was based on the interest of helping people living in paris to be able to estimate the cost of house, inorder make better decisons, as houses are quite expensive in the area 


final deployment available  on   [paris-prediction](https://paris-housing-prediction.herokuapp.com/)

conda enviroment was used for this project:
before we start the project, we create a conda environment installing all the dependencies 
	from conda base
	
		#we run the follwing command: 
			conda env create -f environment.yml  -> creates a conda environment with the enviroment.yml file
			conda activate project -> this activate the projects environment created in the enviroment.yml file
		    make setup -> the runs the setup in the make file, installing all the dependencies to our new environment

			NOTE
			#to make the environment we crate available in jupyter notebook
				-> conda install nb_conda_kernels

NOTES:
	the commands is yellow are to be run with in the cli 
	ensure terminals(cli) are in the same folder and the environment is always activated
	a more detailed readme on each individual process has been included in each folder 


DATASET  [kaggle dataset](https://www.kaggle.com/datasets/mssmartypants/paris-housing-price-prediction)
we create an infrastructure for the terraform-state for the backend 
we crate a bucket to store our dataset using terraform
we execute a python script, that gets data from kaggle, sort the data by years, divides the data into 4 and uploades it into our s3 bucket


MODEL CHOOSING
we move to the choosing of model 
we read the data directly from our bucket using the boto python library 
we do some exploratory data analysis to see which features that influence the house prices 
we used different algorithms and chose the best using model registry

ORCHESTRATION
orchestration with prefect, model registry to choose best training mmodel and teting 
we automated and deployed the job using prefect 2.0.3 (there might be a newer version)

WEBSERVICE
first we test the predict.py file with test.py 
and the we use docker to build the file and run it 


MONITORING
we use both the online monitoring with prometheus and grafana, using evidently ai 
we have a report generated which is available evidently_report_example.html in the same folder

FLASK-DEPLOYMENT
 here we run flask tests, to test the routes of the file we are going to deploy and to makesure all the error checks are avoided 
 the test are done using pytest, and files can be found in the flask folder, in this deployment, we used mongodb clusters as database, so that 
 any input from any user online will go state to our database on the server.
 
 deployment is available  [paris-prediction](https://paris-housing-prediction.herokuapp.com/)



BEST PRACTICES
Makefile
	the make file includes the quality checks and the also the set, which are both activated using 
	
	-> make setup 
		installation of requirements

	-> make quality checks (linting and formatting)
			black pylint sort 
