from sensor.config import mongoclient
import os,sys
from sensor.logger import logging
from sensor.exception import SensorException
import pandas as pd
import yaml
import numpy as np
import dill


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
    

def save_numpy_array(file_path:str,array:np.array):
    """
    Save numpy array data to file
    file_path"str location of file to save
    array:np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_writer:
            np.save(file_writer,array)
    except Exception as e:
        raise SensorException(e,sys)
    
def save_object(file_path:str,obj:object):
    try:
        logging.info("Entered the save object method of utils")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
        logging.info(f"{obj} Object has been successfully saved and exiting now")        
    except Exception as e:
        raise SensorException(e,sys)
    


def load_numpy_array(file_path:str)->np.array:
    try:
        with open(file_path,"rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise SensorException(e,sys)
    

