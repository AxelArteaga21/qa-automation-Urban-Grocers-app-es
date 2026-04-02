import requests
from config import config

def get_logs():
    return requests.get(
        url=f'{config.URL_SERVICE}{config.LOG_MAIN_PATH}',
        params={"count":20}
    )