from flask import Flask, request
from credit_card.exception import CreditCardException
from credit_card.logger import logging, get_log_dataframe
import os, sys
from credit_card.config.configuration import Configuration
from flask import send_file, abort, render_template
from credit_card.pipeline.pipeline import Pipeline
from credit_card.constant import CONFIG_DIR, get_current_time_stamp
from credit_card.entity.credit_card_predictor import Credit_Card_Predictor, CreditCardData
import json
from credit_card.util.util import read_yaml, write_yaml

ROOT_DIR = os.getcwd()
LOG_FOLDER_NAME = 'credit_card_logs'
PIPELINE_FOLDER_NAME = 'credit_card'
SAVED_MODELS_DIR_NAME = 'saved_models'
MODEL_CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, 'model.yaml')
LOG_DIR = os.path.join(ROOT_DIR, LOG_FOLDER_NAME)
PIPELINE_DIR = os.path.join(ROOT_DIR, PIPELINE_FOLDER_NAME)
MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)

CREDIT_CARD_DATA_KEY = "credit_card_data"
DEFAULT_PAYMENT_NEXT_MONTH_KEY = "default_payment_next_month"

app = Flask(__name__)



@app.route('/predict', methods=['GET', 'POST'])
def predict():
    context = {
        CREDIT_CARD_DATA_KEY: None,
        DEFAULT_PAYMENT_NEXT_MONTH_KEY: None
    }

    if request.method == 'POST':
        LIMIT_BAL = int(request.form['LIMIT_BAL'])
        SEX = request.form['SEX']
        EDUCATION = request.form['EDUCATION']
        MARRIAGE = request.form['MARRIAGE']
        AGE = int(request.form['AGE'])
        PAY_0 = request.form['PAY_0']
        PAY_2 = request.form['PAY_2']
        PAY_3 = request.form['PAY_3']
        PAY_4 = request.form['PAY_4']
        PAY_5 = request.form['PAY_5']
        PAY_6 = request.form['PAY_6']
        BILL_AMT1 = int(request.form['BILL_AMT1'])
        BILL_AMT2 = int(request.form['BILL_AMT2'])
        BILL_AMT3 = int(request.form['BILL_AMT3'])
        BILL_AMT4 = int(request.form['BILL_AMT4'])
        BILL_AMT5 = int(request.form['BILL_AMT5'])
        BILL_AMT6 = int(request.form['BILL_AMT6'])
        PAY_AMT1 = int(request.form['PAY_AMT1'])
        PAY_AMT2 = int(request.form['PAY_AMT2'])
        PAY_AMT3 = int(request.form['PAY_AMT3'])
        PAY_AMT4 = int(request.form['PAY_AMT4'])
        PAY_AMT5 = int(request.form['PAY_AMT5'])
        PAY_AMT6 = int(request.form['PAY_AMT6'])

        credit_card_data = CreditCardData(
            LIMIT_BAL=LIMIT_BAL,
            SEX=SEX,
            EDUCATION=EDUCATION,
            MARRIAGE=MARRIAGE,
            AGE=AGE,
            PAY_0=PAY_0,
            PAY_2 = PAY_2,
            PAY_3=PAY_3,
            PAY_4=PAY_4,
            PAY_5=PAY_5,
            PAY_6=PAY_6,
            BILL_AMT1=BILL_AMT1,
            BILL_AMT2=BILL_AMT2,
            BILL_AMT3=BILL_AMT3,
            BILL_AMT4=BILL_AMT4,
            BILL_AMT5=BILL_AMT5,
            BILL_AMT6=BILL_AMT6,
            PAY_AMT1=PAY_AMT1,
            PAY_AMT2=PAY_AMT2,
            PAY_AMT3=PAY_AMT3,
            PAY_AMT4=PAY_AMT4,
            PAY_AMT5=PAY_AMT5,
            PAY_AMT6=PAY_AMT6)
        credit_card_df = credit_card_data.credit_card_input_data_frame()
        credit_card_predictor = Credit_Card_Predictor(model_dir=MODEL_DIR)
        default_payment_next_month = credit_card_predictor.predict(X=credit_card_df)
        context = {
            CREDIT_CARD_DATA_KEY: credit_card_data.get_credit_card_data_as_dict(),
            DEFAULT_PAYMENT_NEXT_MONTH_KEY: default_payment_next_month,
        }
        return render_template('predict.html', context=context)
    return render_template("predict.html", context=context)
    
if __name__ == "__main__":
    app.run()