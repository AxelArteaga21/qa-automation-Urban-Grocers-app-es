import requests
from config import config

def create_new_user(user_body):
    current_header = {
          "Content-Type": "application/json",
    }
    return requests.post(
        url=f'{config.URL_SERVICE}{config.CREATE_USER_PATH}',
        json=user_body,
        headers=current_header
    )