from api.user_api import create_new_user
from api.table_api import get_table_model

import pytest

@pytest.mark.parametrize("body, expected_status, error_message",[
    ({
        "firstName": "Aa",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
     },201, None),
    ({
        "firstName": "Aaaaaaaaaaaaaaa",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
     },201, None),
    ({
        "firstName": "a",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
     }, 400, "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."),
    ({
        "firstName": "Aaaaaaaaaaaaaaaa",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
     },400,"Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."),
    ({
         "firstName": "A Aaa",
         "phone": "+10005553535",
         "address": "8042 Lancaster Ave.Hamburg, NY"
     }, 400,
     "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."),
    ({
         "firstName": "\"№%@\",",
         "phone": "+10005553535",
         "address": "8042 Lancaster Ave.Hamburg, NY"
     }, 400,
     "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."),
    ({
         "firstName": "123",
         "phone": "+10005553535",
         "address": "8042 Lancaster Ave.Hamburg, NY"
     }, 400,
     "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."),
    ({
         "phone": "+10005553535",
         "address": "8042 Lancaster Ave.Hamburg, NY"
     }, 400,
     "No se han aprobado todos los parámetros requeridos"),
    ({
         "firstName": "",
         "phone": "+10005553535",
         "address": "8042 Lancaster Ave.Hamburg, NY"
     }, 400,
     "No se han aprobado todos los parámetros requeridos"),
    ({
         "firstName": 12,
         "phone": "+10005553535",
         "address": "8042 Lancaster Ave.Hamburg, NY"
     }, 400,None),

])
def test_create_user(body, expected_status, error_message):
    response = create_new_user(body)

    assert response.status_code == expected_status

    if expected_status == 201:
        assert "authToken" in response.json()
        assert response.json()["authToken"] != ""

        data_base = get_table_model("user_model")

        str = f'{body["firstName"]},{body["phone"]},{body["address"]},,,{response.json()["authToken"]}'

        assert data_base.text.count(str) == 1

    if expected_status == 400:
        if error_message is not None:
            assert error_message in response.json()["message"]
        assert "code" in response.json()
        assert response.json()["code"] == 400


