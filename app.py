from flask import Flask
from credit_card.exception import CreditCardException
from credit_card.logger import logging
import sys

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    try:
        raise Exception('App is not running')
    except Exception as e:
        credit = CreditCardException(e, sys)
        logging.error(credit)


if __name__ == '__main__':
    app.run()