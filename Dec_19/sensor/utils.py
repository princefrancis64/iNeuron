from sensor.config import mongoclient
import os,sys
from sensor.logger import logging
from sensor.exception import SensorException
import pandas as pd
import yaml


def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: This function returns collection as dataframe
    ==========================================================
    Params:
    database_name:database_name
    collection_nanme:collection_name
    ==========================================================
    returns pandas dataframe of the collection
    """
    try:
        logging.info(f"Reading dataframe from mongodb database {database_name} and collection {collection_name}")
        df = pd.DataFrame(list(mongoclient[database_name][collection_name].find()))
        logging.info(f"Found columns {df.columns}")
        if "_id" in df:
            df=  df.drop("_id",axis= 1)
        logging.info(f"Rows and columns in df:{df.shape}")
        return df
    except Exception as e:
        raise SensorException(e,sys)
    

def convert_column_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:
        for column in df.columns:
            if column not in exclude_columns:
                df[column] = df[column].astype('float')
        return df
    except Exception as e:
        raise SensorException(e,sys)
    
def write_yaml_file(file_path:str,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as e:
        raise SensorException(e,sys)