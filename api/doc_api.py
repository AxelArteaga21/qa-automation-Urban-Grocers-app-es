import requests
from config import config

def get_document():
    return requests.get(
        url=f'{config.URL_SERVICE}{config.DOC_PATH}'
    )