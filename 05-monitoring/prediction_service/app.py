import os
import pickle

import requests
from flask import Flask, jsonify, request
from pymongo import MongoClient

# we loadthe model here
MODEL_FILE = os.getenv("MODEL_FILE", "model-lin.b")


# we connect to the mongo database  and connect evidently to mongo db
# cluster = MongoClient("mongodb+srv://deen360:1_Jackson5@cluster0.zyfi4dh.mongodb.net/?retryWrites=true&w=majority")
# EVIDENTLY_SERVICE_ADDRESS = os.getenv('EVIDENTLY_SERVICE', "mongodb+srv://deen360:1_Jackson5@cluster0.zyfi4dh.mongodb.net/?retryWrites=true&w=majority")
# MONGODB_ADDRESS = os.getenv("MONGODB_ADDRESS", "mongodb+srv://deen360:1_Jackson5@cluster0.zyfi4dh.mongodb.net/?retryWrites=true&w=majority")

EVIDENTLY_SERVICE_ADDRESS = os.getenv("EVIDENTLY_SERVICE", "http://127.0.0.1:5000")
MONGODB_ADDRESS = os.getenv("MONGODB_ADDRESS", "mongodb://127.0.0.1:27017")

with open(MODEL_FILE, "rb") as f_in:
    dv, model = pickle.load(f_in)


app = Flask("prices")
mongo_client = MongoClient(MONGODB_ADDRESS)

# db =cluster["flask"]
db = mongo_client.get_database("prediction_service")

# collection = db["parisprediction"]
collection = db.get_collection("data")


@app.route("/predict", methods=["POST"])
def predict():
    record = request.get_json()

    features = {}
    features["squareMeters"] = record["squareMeters"]
    # record = record['squareMeters']
    X = dv.transform(features)
    y_pred = model.predict(X)
    y_pred = round(y_pred[0])
    result = {
        "House price": y_pred,
    }

    save_to_db(record, y_pred)
    send_to_evidently_service(record, y_pred)
    return jsonify(result)


def save_to_db(record, prediction):
    rec = record.copy()
    rec["prediction"] = prediction
    collection.insert_one(rec)


def send_to_evidently_service(record, prediction):
    rec = record.copy()
    rec["prediction"] = prediction
    requests.post(f"{EVIDENTLY_SERVICE_ADDRESS}/iterate/paris", json=[rec])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
