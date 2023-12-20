import pymongo
import os
import json
from dataclasses import dataclass


@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    

env_var = EnvironmentVariable()
mongoclient = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = 'class'