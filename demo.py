from credit_card.logger import logging
from credit_card.exception import CreditCardException
from credit_card.config.configuration import Configuration
import sys



def main():
    try:
        config = Configuration()
        data_ingestion_artifact = config.get_data_ingestion_config()
        print(data_ingestion_artifact)
    except Exception as e:
        logging.error(f'{e}')
        print(e)
if __name__ == '__main__':
    main()