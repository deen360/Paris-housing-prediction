
in choosing the right model

Firstly, we load the data we create in "01-dataset" from our s3 bucket
convert the  csv file to parquet format as parquet format improves efficiency 

we choose our target feature which in this cas is the Price of the house, 
then we do some exploratory data analsyis(EDA) and  some satistical analysis to see which features of the dataset we want to include in our analysis,  from the EDA and the pearsons correlation, the squaremeters seems to have a very strong correlation with the price of the house, where the line is was linear. this prompted the decision to proceed with a linear model for our analaysis, as adding other features didnt make any significant difference

in the experiments, we used Three algorithms namely
linear rigression 
lasso rigression
ridge rigression

each of  which had a similar mae  so we convert each model to a python script, so that we can use them in the registry to select the best model using mlflow for the experiment tracking 


MLflow and registry Registry models:
here we have 3 python scripts where we have included the mlflow sklearn autolog function, so that the metics can be taken when the files are logged 
mlflow_lasso.py -> which is the lasso model
mlflow_linear.py -> which is the linear model
mlflow_ridge.py -> which is the ridge model 

first we start the ml flow using sqlite as a datebase to register the model runs 
by running 
# mlflow server --backend-store-uri sqlite:///backend.db --default-artifact-root artifacts_local
then we open the mlflow ui at http://127.0.0.1:5000
we run the models each
        python mlflow_lasso.py 
        python mlflow_linear.py 
        python mlflow_ridge.py

we check the mlflow ui, and we have 3 different models under "my-experiment-1" logged.  there are 1 models from lasso model, linear model and ridge model respectively 

we the open the Registry Jupyter-notebook -> Registry.ipynb to select the best model
the linear regression model was chosen since they all has the same rmse and the linear regression model had the least training to, the model 
was the saved a model-lin.b

the 2 parameters we saved in the model-lin.b are the Dictvectorizer(dv) and the linear regression model(model)

