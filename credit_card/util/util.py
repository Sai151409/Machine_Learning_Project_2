from credit_card.exception import CreditCardException
from credit_card.logger import logging
import yaml
import os, sys


def read_yaml(file_path:str):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise CreditCardException(e, sys) from e