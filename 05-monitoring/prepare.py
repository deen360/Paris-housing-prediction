import boto3
import requests
from tqdm import tqdm
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


files = [
    ("ParisHousing_period_04.parquet", "."),
    ("ParisHousing_period_01.parquet", "./evidently_service/datasets"),
]


print(f"Download files:")
for file, path in files:
    url = f"https://mlops-project-dataset-deen.s3.eu-west-3.amazonaws.com/paris-housing-dataset/{file}"
    resp = requests.get(url, stream=True)
    print(resp)
    save_path = f"{path}/{file}"
    with open(save_path, "wb") as handle:
        for data in tqdm(
            resp.iter_content(),
            desc=f"{file}",
            postfix=f"save to {save_path}",
            total=int(resp.headers["Content-Length"]),
        ):
            handle.write(data)
