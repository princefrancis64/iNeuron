from sensor.entity import config_entity,artifact_entity
from sensor.components.data_ingestion import DataIngestion



if __name__=="__main__":
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        print("Training",training_pipeline_config)

        #data ingestion
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print("Data ingestion config " ,data_ingestion_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        print(e)