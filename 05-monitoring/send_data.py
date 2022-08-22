import io
import json
import uuid
from time import sleep
from datetime import datetime

import requests
import pyarrow.parquet as pq

table = pq.read_table("ParisHousing_period_04.parquet")
data = table.to_pylist()


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


with io.open("target.csv", "w", encoding="utf-8") as f_target:
    for row in data:
        row["id"] = str(uuid.uuid4())
        squareMeters = row["squareMeters"]

        if squareMeters != 0:
            f_target.write(f"{row['id']},{squareMeters}\n")
        resp = requests.post(
            "http://127.0.0.1:9696/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(row, cls=DateTimeEncoder),
        ).json()
        print(f"prediction: {resp['House price']}")
        sleep(1)
