from sensor.config import mongoclient
import sys
from sensor.logger import logging
from sensor.exception import SensorException
import pandas as pd

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