import io
import os
import json
import pickle

import pandas
import pyarrow.parquet as pq
from prefect import flow, task
from pymongo import MongoClient
from evidently import ColumnMapping
from evidently.dashboard import Dashboard
from evidently.model_profile import Profile
from evidently.dashboard.tabs import DataDriftTab, RegressionPerformanceTab
from evidently.model_profile.sections import (
    DataDriftProfileSection,
    RegressionPerformanceProfileSection,
)


# here we are loading reading each line in the file and we are using set to inpu the data
@task
def upload_target(filename):
    client = MongoClient("mongodb://localhost:27018/")
    collection = client.get_database("prediction_service").get_collection("data")
    with io.open(filename, encoding="utf-8") as f_target:
        for line in f_target.readlines():
            row = line.split(",")
            collection.update_one({"id": row[0]}, {"$set": {"target": float(row[1])}})
    client.close()


# we are opening the model, reading the file a dataframe, choosing the x-axis parameters(sqauremeters) and y-axis as target,
# we also transfor the x-values to a dictinary before we use it to predict
@task
def load_reference_data(filename):
    MODEL_FILE = os.getenv("MODEL_FILE", "./prediction_service/model-lin.b")
    with open(MODEL_FILE, "rb") as f_in:
        dv, model = pickle.load(f_in)
    reference_data = pq.read_table(filename).to_pandas()
    # Create features
    # reference_data['PU_DO'] = reference_data['PULocationID'].astype(str) + "_" + reference_data['DOLocationID'].astype(str)

    # reference_data['squareMeters'] = reference_data['squareMeters']

    # add target column
    # reference_data['target'] = reference_data.lpep_dropoff_datetime - reference_data.lpep_pickup_datetime
    reference_data["target"] = reference_data["price"]

    # reference_data.target = reference_data.target.apply(lambda td: td.total_seconds() / 60)
    # reference_data = reference_data[(reference_data.target >= 1) & (reference_data.target <= 60)]
    reference_data = reference_data[(reference_data.target >= 1)]

    # features = ['PU_DO', 'PULocationID', 'DOLocationID', 'trip_distance']
    features = ["squareMeters"]
    x_pred = dv.transform(reference_data[features].to_dict(orient="records"))
    reference_data["prediction"] = model.predict(x_pred)
    return reference_data


@task
def fetch_data():
    client = MongoClient("mongodb://localhost:27018/")
    data = client.get_database("prediction_service").get_collection("data").find()
    df = pandas.DataFrame(list(data))
    return df


# here we calculate the json prorfile, verbose level is made equal to 0 to keep it short and 1 to br huge
@task
def run_evidently(ref_data, data):
    # ref_data.drop('ehail_fee', axis=1, inplace=True)
    # data.drop('ehail_fee', axis=1, inplace=True)
    # drop empty column (until Evidently will work with it properly)

    profile = Profile(sections=[DataDriftProfileSection(), RegressionPerformanceProfileSection()])
    # mapping = ColumnMapping(prediction="prediction", numerical_features=['trip_distance'],
    #                        categorical_features=['PULocationID', 'DOLocationID'],
    #                        datetime_features=[])

    mapping = ColumnMapping(
        prediction="prediction",
        numerical_features=["squareMeters"],
        datetime_features=[],
    )

    profile.calculate(ref_data, data, mapping)

    dashboard = Dashboard(tabs=[DataDriftTab(), RegressionPerformanceTab(verbose_level=0)])
    dashboard.calculate(ref_data, data, mapping)
    return json.loads(profile.json()), dashboard


@task
def save_report(result):
    client = MongoClient("mongodb://localhost:27018/")
    client.get_database("prediction_service").get_collection("report").insert_one(result[0])


@task
def save_html_report(result):
    result[1].save("evidently_report_example.html")


@flow
def batch_analyze():
    upload_target("target.csv")
    # work
    ref_data = load_reference_data("./evidently_service/datasets/ParisHousing_period_01.parquet")
    data = fetch_data()
    result = run_evidently(ref_data, data)
    save_report(result)
    save_html_report(result)


batch_analyze()
