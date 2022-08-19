
import pandas as pd
import s3fs
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import Ridge
import mlflow
import pickle

#the server you create will run on this address, 
#we are setting the tracking unit to this address 
mlflow.set_tracking_uri("http://127.0.0.1:5000")
#experiment name 
mlflow.set_experiment("my-experiment-1")

         
mlflow.sklearn.autolog()

mlflow.set_tag("developer", "yusuf")

def read_dataframe(filename):
    #we read the file
    if filename.endswith('.parquet'):
        df = pd.read_parquet(filename)
    #we are using the squaremeter as feature for the model
    return  df    

#we you period 1 as our training dataset 
i = 1
input_file = f"s3://mlops-project-dataset-deen/paris-housing-dataset/ParisHousing_period_{i:02d}.parquet"
df_train = read_dataframe(input_file)

#we use period 2 as our validation dataset
i = 2
file = f"s3://mlops-project-dataset-deen/paris-housing-dataset/ParisHousing_period_{i:02d}.parquet"
df_val = read_dataframe(file)

mlflow.log_param("train-data-path", "s3://mlops-project-dataset-deen/paris-housing-dataset/ParisHousing_period_01.parquet")

mlflow.log_param("valid-data-path","s3://mlops-project-dataset-deen/paris-housing-dataset/ParisHousing_period_02.parquet")

#we choose the feature here 
categorical = ['squareMeters']
df_train_data = df_train[categorical]
df_val_data = df_val[categorical]

#we convert the columns to a dictionary
train_dicts = df_train_data[categorical].to_dict(orient='records')
val_dicts = df_train_data[categorical].to_dict(orient='records')



#dictionary to vector converter
dv = DictVectorizer()

#dictionary to vector conversion, here we use fit because its for training
X_train = dv.fit_transform(train_dicts)

#here we use transorm because its for validation
X_val = dv.transform(val_dicts)


#for this model, our interest is the price of the house 
target = 'price'
y_train = df_train[target].values
y_val = df_val[target].values




#Using ridge regressor
regressor_Ridge = Ridge(alpha=0.012)

#we fit the model
regressor_Ridge.fit(X_train, y_train)

y_pred = regressor_Ridge.predict(X_val)

mean_squared_error(y_val, y_pred, squared=False)


rmse = mean_squared_error(y_val, y_pred, squared=False)
mlflow.log_metric("rmse", rmse)

filename = "models/ridge-reg"
pickle.dump((dv,regressor_Ridge), open(filename,'wb'))

mlflow.log_artifact(local_path="models/ridge-reg", artifact_path="_local_models_pickle")