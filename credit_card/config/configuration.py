import os, sys
from credit_card.entity.config_entity import DataIngestionConfig, DataValidationConfig, \
    DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig, \
    ModelPusherConfig, TrainingPipelineConfig
from credit_card.constant import *
from credit_card.exception import CreditCardException
from credit_card.logger import logging
from credit_card.util.util import read_yaml


class Configuration:
    
    def __init__(self, config_file_path : str = CONFIG_FILE_PATH,
                 time_stamp : str =  CURRENT_TIME_STAMP) -> None:
        try:
            self.config = read_yaml(file_path=config_file_path)
            self.time_stamp = time_stamp
            self.training_pipeline_artifact = self.get_pipeline_config()
        except Exception as e:
            raise CreditCardException(e, sys) from e
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_artifact.artifact_dir
            data_ingestion_info = self.config[DATA_INGESTION_CONFIG_KEY]
            download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            data_ingestion_artifact = os.path.join(artifact_dir, DATA_INGESTION_ARTIFACT_KEY)
            raw_data_dir = os.path.join(
                data_ingestion_artifact, data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )
            ingested_train_dir = os.path.join(
                data_ingestion_artifact,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_KEY],
                data_ingestion_info[DATA_INGESTION_INGESTED_TRAIN_DIR_KEY]
            )
            ingested_test_dir = os.path.join(
                data_ingestion_artifact,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_KEY],
                data_ingestion_info[DATA_INGESTION_INGESTED_TEST_DIR_KEY]
            )
            
            data_ingestion_config = DataIngestionConfig(
                download_url=download_url,
                raw_data_dir=raw_data_dir, 
                ingested_train_dir=ingested_train_dir,
                ingested_test_dir=ingested_test_dir
            )
            
            logging.info(f'Data Ingestion Config : {data_ingestion_config}')
            
            return data_ingestion_config
        except Exception as e:
            raise CreditCardException(e, sys) from e 
    
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            pass
        except Exception as e:
            raise CreditCardException(e, sys) from e 
        
    def get_data_transformation_config(self)-> DataTransformationConfig:
        try:
            pass
        except Exception as e:
            raise CreditCardException(e, sys) from e 
        
    def get_model_trainer_config(self)-> ModelTrainerConfig:
        try:
            pass
        except Exception as e:
            raise CreditCardException(e, sys) from e 
        
    def get_model_evalutaion_config(self) -> ModelEvaluationConfig:
        try:
            pass
        except Exception as e:
            raise CreditCardException(e, sys) from e 
    
    def get_model_pusger_config(self) -> ModelPusherConfig:
        try:
            pass
        except Exception as e:
            raise CreditCardException(e, sys) from e 
    
    def get_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_info = self.config[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(
                ROOT_DIR,
                training_pipeline_info[TRAINING_PIPELINE_NAME_KEY],
                training_pipeline_info[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )
            
            training_pipeline_artifact = TrainingPipelineConfig(
                artifact_dir=artifact_dir
            )
            
            logging.info(f'Training Pipeline Artifact : {training_pipeline_artifact}')
            
            return training_pipeline_artifact
            
        except Exception as e:
            raise CreditCardException(e, sys) from e 