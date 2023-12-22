from sensor.entity import config_entity,artifact_entity
import pandas as pd,numpy as np
import os,sys
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.predictor import ModelResolver
from sensor.utils import load_obj
from sensor.config import TARGET_COLUMN
from sklearn.metrics import f1_score

class ModelEvaluation:

    def __init__(self,
                 model_eval_config:config_entity.ModelEvaluationConfig,
                 data_ingestion_artifact:artifact_entity.DataIngestionArtifact,
                 data_transformation_artifact:artifact_entity.DataTransformationArtifact,
                 model_trainer_artifact:artifact_entity.ModelTrainerArtifact):
        try:
            logging.info(f"{'>>'*20} Model Evaluation{'<<'*20}")
            self.model_eval_config = model_eval_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.model_resolver = ModelResolver()
        except Exception as e:
            raise SensorException(e,sys)
        

    def initiate_model_evaluation(self)->artifact_entity.ModelEvaluationArtifact:
        try:
            logging.info("if saved_models folder has saved model then we will compare it or else we will train new model and save it")
            latest_dir_path = self.model_resolver.get_latest_dir_path()
            if latest_dir_path==None:
                model_eval_artifact= artifact_entity.ModelEvaluationArtifact(is_model_accepted=True,improved_accuracy=None)
                logging.info(f"Model Evaluation artifact is {model_eval_artifact}")
                return model_eval_artifact
            
            #Finding location of latest transformer, model and targer encoder in the saved_foler
            logging.info("Finding location of transformer,model and target_encoder")
            transformer_path = self.model_resolver.get_latest_transformer_path()
            model_path = self.model_resolver.get_latest_model_path()
            target_encoder_path = self.model_resolver.get_latest_target_encoder_path()
            print(target_encoder_path)

            logging.info("Loading the previously saved models,transformer and target_encoder in the latest file path")
            transformer = load_obj(file_path=transformer_path)
            model = load_obj(file_path=model_path)
            target_encoder = load_obj(file_path=target_encoder_path)

            logging.info("Checking out currently trained objects")
            current_transformer = load_obj(file_path=self.data_transformation_artifact.transform_object_path)
            current_model = load_obj(file_path=self.model_trainer_artifact.model_file_path)
            current_target_encoder= load_obj(file_path=self.data_transformation_artifact.target_encoder_path)

            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            target_df = test_df[TARGET_COLUMN]
            print(target_df.head())
            print(type(target_encoder))
            print(target_encoder)
            y_true = target_encoder.transform(target_df)

            #accuracy using previously trained model
            input_feature_name = list(transformer.feature_names_in_)
            input_arr = transformer.transform(test_df[input_feature_name])
            y_pred = model.predict(input_arr)
            logging.info(f"Prediction using previous model:{target_encoder.inverse_transform(y_pred[:5])}")
            previous_model_score = f1_score(y_true=y_true,y_pred=y_pred)
            logging.info(f"Accuracy using previously trained model {previous_model_score}")

            #accuracy using current trained model
            input_feature_name = list(current_transformer.feature_names_in_)
            input_arr = current_transformer.transform(test_df[input_feature_name])
            y_pred = current_model.predict(input_arr)
            y_true = current_target_encoder.transform(target_df)
            logging.info(f"Prediction using current model:{current_target_encoder.inverse_transform(y_pred[:5])}")
            current_model_score = f1_score(y_true=y_true,y_pred=y_pred)
            logging.info(f"Accuracy using current trained model:{current_model_score}")
            if current_model_score<=previous_model_score:
                logging.info("Current trained model is not better than previous model")
                raise Exception("Current trained model is not better than previous model")

            model_eval_artifact= artifact_entity.ModelEvaluationArtifact(is_model_accepted=True,
                                                    improved_accuracy= current_model_score-previous_model_score)
            logging.info(f"Model eval artifact {model_eval_artifact}")
            return model_eval_artifact            
        except Exception as e:
            raise SensorException(e,sys)