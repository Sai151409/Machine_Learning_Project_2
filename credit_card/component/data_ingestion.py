from credit_card.logger import logging
from credit_card.exception import CreditCardException
import os, sys
from credit_card.entity.config_entity import DataIngestionConfig
from six.moves import urllib
from credit_card.entity.artifact_entity import DataIngestionArtifact
import pandas as pd


class DataIngestion:
    
    def __init__(self, data_ingestion_config : DataIngestionConfig):
        try:
            logging.info(f'{"==" * 30} Data Ingestion log started {"==" * 30}')
            self.data_ingestion_config = data_ingestion_config  
        except Exception as e:
            raise CreditCardException(e, sys) from e
        
    def download_credit_card_dataset(self):
        try:
            download_url = self.data_ingestion_config.download_url
            
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)
            
            os.makedirs(raw_data_dir, exist_ok=True)
            
            urllib.request.urlretrieve(download_url, raw_data_dir)
            
            logging.info(f'Downloading the dataset form {download_url} to {raw_data_dir}')
            
            file_name = os.listdir(raw_data_dir)[0]
            
            raw_data_file_path = os.path.join(raw_data_dir, file_name)
            
            return raw_data_file_path
        except Exception as e:
            raise CreditCardException(e, sys) from e
        
    def split_data_as_train_test(self, raw_data_file_path  :str) -> DataIngestionArtifact:
        try:
            credit_card_dataset_file_path = raw_data_file_path
            
            credit_card_dataframe = pd.read_csv(credit_card_dataset_file_path)
            
            logging.info('Splitting the dataset into train and test')
            
            start_train = None
            strat_test = None
            
            
            
        except Exception as e:
            raise CreditCardException(e, sys) from e