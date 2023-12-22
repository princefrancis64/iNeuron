import os,sys
from sensor.logger import logging
from sensor.exception import SensorException
import pandas as pd
import numpy as np
from sensor.predictor import ModelResolver
from sensor.utils import load_obj
from datetime import datetime

PREDICTION_DIR = "prediction"

def start_batch_prediction(input_file_path):
    try:
        os.makedirs(PREDICTION_DIR,exist_ok=True)
        logging.info("Creating model resolver object")
        model_resolver = ModelResolver()
        logging.info(f"Reading file :{input_file_path}")
        df = pd.read_csv(input_file_path)
        df.replace({"na":np.NAN},inplace=True)

        #validation

        logging.info("Logging transformer to transform object")
        transformer  = load_obj(file_path=model_resolver.get_latest_transformer_path())

        input_feature_names = list(transformer.feature_names_in_)
        input_arr = transformer.transform(df[input_feature_names])

        logging.info("Loading model to make prediction")
        model =load_obj(file_path=model_resolver.get_latest_model_path())
        prediction = model.predict(input_arr)

        logging.info("Loading target encoder to transform predicted columns into categorical")
        target_encoder = load_obj(file_path=model_resolver.get_latest_target_encoder_path())

        cat_prediction =  target_encoder.inverse_transform(prediction)

        df['prediction']=prediction
        df['cat_prediction']=cat_prediction

        prediction_file_name = os.path.basename(input_file_path).replace("csv",f"_{datetime.now().strftime('%m%d%Y__%H%M%S')}.csv")
        prediction_file_path = os.path.join(PREDICTION_DIR,prediction_file_name)
        df.to_csv(prediction_file_path,index=False,header=True)
        return prediction_file_path
    except Exception as e:
        raise SensorException(e,sys)