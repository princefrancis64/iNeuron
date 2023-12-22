from asyncio import tasks
import json
from textwrap import dedent
import pendulum
import os
from airflow import DAG
from airflow.operators.python import PythonOperator


with DAG(
    'sensor_training',
    default_args={'retries': 2},
    # [END default_args]
    description='Sensor Fault Detection',
    schedule_interval="@weekly",
    start_date=pendulum.datetime(2023, 12, 17, tz="UTC"),
    catchup=False,
    tags=['example'],
) as dag:

    def download_files(**kwargs):
        bucket_name = os.getenv("BUCKET_NAME")
        input_dir = "/app/input_files"
        #creating directory
        os.makedirs(input_dir,exist_ok=True)
        os.system(f"aws s3 sync s3://{bucket_name}/input_files/app/input_files")

    

