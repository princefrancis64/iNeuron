from sensor.predictor import ModelResolver
from sensor.entity import config_entity,artifact_entity
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys
from sensor.utils import save_object,load_obj


class ModelPusher:

    def __init__(self,model_pusher_config:config_entity.ModelPusherConfig,
                 data_transformation_artifact:artifact_entity.DataTransformationArtifact,
                 model_trainer_artifact:artifact_entity.ModelTrainerArtifact):
        try:
            logging.info(f"{'>>'*20} Model Pusher {'<<'*20}")
            self.model_pusher_config = model_pusher_config
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.model_resolver = ModelResolver(model_registry=self.model_pusher_config.saved_model_dir)
        except Exception as e:
            raise SensorException(e,sys)
        

    def initiate_model_pusher(self,)->artifact_entity.ModelEvaluationArtifact:
        try:
            #Loading the object from artifacts of each components
            logging.info("Loading the object from artifact/model pusher folder")
            transformer = load_obj(file_path=self.data_transformation_artifact.transform_object_path)
            model = load_obj(file_path=self.model_trainer_artifact.model_file_path)
            target_encoder = load_obj(file_path=self.data_transformation_artifact.target_encoder_path)
            

            #Now Saving the loaded objects into artifact/saved_models/model,artifact/saved_models/transformer and artifact/saved_models/target_encoder
            logging.info("Now Saving the loaded objects into artifact/saved_models/model,artifact/saved_models/transformer and artifact/saved_models/target_encoder")
            save_object(file_path=self.model_pusher_config.pusher_model_path,obj=model)
            save_object(file_path=self.model_pusher_config.pusher_transformer_path,obj=transformer)
            save_object(file_path=self.model_pusher_config.pusher_target_encoder_path,obj=target_encoder)

            #Getting the model, transformer and target_encoder path to save in saved_models dir
            logging.info("Getting the  model, transformer and target_encoder path to save in saved_models dir")
            transformer_path = self.model_resolver.get_latest_save_transformer_path()
            model_path = self.model_resolver.get_latest_save_model_path()
            target_encoder_path = self.model_resolver.get_latest_save_target_encoder_path()

            #Saving the model, transformer and target_encoder to saved_models dir
            logging.info("Saving the model, transformer and target_encoder to saved_models dir")
            save_object(file_path=transformer_path,obj=transformer)
            save_object(file_path=model_path,obj=model)
            save_object(file_path=target_encoder_path,obj=target_encoder)

            model_pusher_artifact = artifact_entity.ModelPusherArtifact(
                pusher_model_dir=self.model_pusher_config.pusher_model_dir,
                saved_model_dir=self.model_pusher_config.saved_model_dir
            )
            logging.info(f"Model Pusher Artifact: {model_pusher_artifact}")
            return model_pusher_artifact
        except Exception as e:
            raise SensorException(e,sys)