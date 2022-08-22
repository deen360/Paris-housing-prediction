#!/usr/bin/env python
# coding: utf-8


import logging
from subprocess import call

import boto3
import numpy as np
import pandas as pd
from botocore.exceptions import ClientError

# we run the script where we have written dowload of the kaggle dataset by using kaggle api
# the file will be downloaded to the current folder where you have this script
rc = call("./script.sh", shell=True)


# we are writing a fuction to help us load the file to aws s3 bucket
def upload_file(file_name, bucket, object_name=None):
    # Upload the file
    s3_client = boto3.client("s3")
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    print("uploaded {} to bucket {} ".format(object_name, bucket))


# here the function converts the file to parquet and uploads to the s3 bucket
def convert_to_parquet(dataset):
    for i in range(len(dataset)):
        dataset[i].to_parquet(f"data/ParisHousing_period_{i + 1:02d}.parquet")

        file_name = f"/home/deen/Desktop/datatalks/mlops-project/01-dataset/python_script/data/ParisHousing_period_{i + 1:02d}.parquet"
        bucket = "mlops-project-dataset-deen"
        object_name = f"paris-housing-dataset/ParisHousing_period_{i + 1:02d}.parquet"
        upload_file(file_name, bucket, object_name)


# we state the location the of the downloaded file, sort it by date and reset the indexes
path = "./ParisHousingClass.csv"
df = pd.read_csv(path)
df.sort_values(by=["made"], inplace=True)
df = df.reset_index()

# here we split the file into four equal parts, so that we can act like the file comes at the end of every period
np.split(df, 4)
period_01 = np.split(df, 4)[0]
period_02 = np.split(df, 4)[1]
period_03 = np.split(df, 4)[2]
period_04 = np.split(df, 4)[3]


# we create inset the tables into an array called data
data = [period_01, period_02, period_03, period_04]


# we call the fuction "convert to parquet that we created above "
convert_to_parquet(data)
