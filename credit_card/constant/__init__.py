import os
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


CURRENT_TIME_STAMP = get_current_time_stamp()
CONFIG_FILE_NAME = 'config.yaml'
CONFIG_DIR = 'config'
ROOT_DIR = os.getcwd()
os.makedirs(CONFIG_DIR, exist_ok=True)

CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)

TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_NAME_KEY = 'pipeline_name'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = 'artifact_dir'

#Data Ingestion related variables

DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
DATA_INGESTION_ARTIFACT_KEY = 'data_ingestion'
DATA_INGESTION_DOWNLOAD_URL_KEY = 'download_url'
DATA_INGESTION_RAW_DATA_DIR_KEY = 'raw_data_dir'
DATA_INGESTION_INGESTED_DIR_KEY = 'ingested_dir'
DATA_INGESTION_INGESTED_TRAIN_DIR_KEY = 'ingested_train_dir'
DATA_INGESTION_INGESTED_TEST_DIR_KEY = 'ingested_test_dir'