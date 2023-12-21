from sensor.entity import config_entity,artifact_entity
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation


if __name__=="__main__":
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        

        #data ingestion
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        #data validation
        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config,)
        data_validation = DataValidation(data_validation_config=data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
        # data_validation_artifact = data_validation.initiate_data_validation()
        data_validation.initiate_data_validation()

        #data transformtion
        data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
        print(data_transformation_config)
        data_transformation = DataTransformation(data_transformation_config=data_transformation_config,data_ingestion_artifact=data_ingestion_artifact)
        print(data_transformation)
        data_transformation_artifact = data_transformation.initiate_data_transformation() 
        
        #model trainer
    except Exception as e:
        print(e)