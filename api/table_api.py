import requests
from config import config

def get_table_model(table_name):
    return requests.get(
        url=f'{config.URL_SERVICE}{config.TABLE_PATH}{table_name}.csv'
    )