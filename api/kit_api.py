import requests
from config.config import URL_SERVICE, KITS_PATH

def create_kit_by_user(kit_body, token):
    current_header = {
          "Content-Type": "application/json",
          "Authorization": f'Bearer {token}'
    }
    return requests.post(
        url=f'{URL_SERVICE}{KITS_PATH}',
        json=kit_body,
        headers=current_header
    )