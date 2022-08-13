first we fetch the dataset from our s3 bucket
then take explore the dataset, so using seaborn al matplotlib, too get an insight of waht the dataset looks like, 
then we run some satistical models on the dataset to determine which feature are important for building our model
then we use one period for test and the other for validation,
we try different machine learnign algorithms and we choose the best one 

to run the ml model
python3 mlflow_linear.py

lasso and ridge models are also availabe
python3 mlflow_lasso.py
python3 mlflow_ridge.py