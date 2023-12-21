from sensor.entity import config_entity,artifact_entity
from sensor.logger import logging 
from sensor.exception import SensorException
from typing import Optional
from sensor import utils
import os,sys
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

class ModelTrainer:

    def __init__(self,data_transformation_artifact:artifact_entity.DataTransformationArtifact,
                 model_trainer_config:config_entity.ModelTrainerConfig):
        try:
            logging.info(f"{'>>'*20} Model Trainer {'<<'*20}")
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    def train_model(self,x,y):
        try:
            xgb_clf = XGBClassifier()
            xgb_clf.fit(x,y)
            return xgb_clf
        except Exception as e:
            raise SensorException(e, sys)
        
    
    def initiate_model_trainer(self)->artifact_entity.ModelTrainerArtifact:
        try:
            logging.info(f"Loading train and test array")
            train_arr = utils.load_numpy_array(file_path=self.data_transformation_artifact.transformed_train_path)
            test_arr = utils.load_numpy_array(file_path=self.data_transformation_artifact.transformed_test_path)

            logging.info(f"Splitting input and target feature from both train and test array")
            X_train,y_train = train_arr[:,:-1],train_arr[:,-1]
            X_test,y_test = test_arr[:,:-1],test_arr[:,-1]

            logging.info(f"Train the model")
            model = self.train_model(x=X_train,y=y_train)

            logging.info(f"Calculating f1 train score")
            yhat_train = model.predict(X_train)
            f1_train_score = f1_score(y_true = y_train,y_pred=yhat_train)

            logging.info("Calculating f1 test score")
            yhat_test = model.predict(X_test)
            f1_test_score = f1_score(y_true = y_test,y_pred=yhat_test)

            logging.info(f"train score:{f1_train_score} and tests score {f1_test_score}")
            #check for overfitting or underfitting or expected score
            logging.info("Checking if our model is underfitted or not")
            if f1_test_score<self.model_trainer_config.expected_score:
                raise Exception(f"Model is not able to give excpected accuracy of {self.model_trainer_config.expected_score}\
                                :Model accuracy is only {f1_test_score}")
            

            logging.info(f"Checking if our model is overfitted or not")
            diff = abs(f1_test_score-f1_train_score)

            if diff>self.model_trainer_config.overfitting_threshold:
                raise Exception(f"Overfitting threshold is more than what is expected that is {self.model_trainer_config.overfitting_threshold}")
            
            #save the trained model
            logging.info(f"Saving model object")
            utils.save_object(file_path=self.model_trainer_config.model_file_path,obj=model)

            #prepare artifact
            logging.info(f"Prepare the artifact")
            model_trainer_artifact = artifact_entity.ModelTrainerArtifact( 
                model_file_path= self.model_trainer_config.model_file_path,
                f1_test_score= f1_test_score,
                f1_train_score= f1_train_score)
            return model_trainer_artifact
        except Exception as e:
            raise SensorException(e,sys)
