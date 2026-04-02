from api.kit_api import create_kit_by_user
from api.user_api import create_new_user
from data import data
import pytest

@pytest.mark.parametrize('body, expected_status, error_message',[
    (
        {
            "name": "a"
        },201,None
    ),
    (
        {
            "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
        },201,None
    ),
    (
        {
            "name": ""
        },400,"No se han aprobado todos los parámetros requeridos"
    ),
    (
        {
            "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
        },400, "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"
    ),
    (
        {
            "name": "\"№%@\","
        },201,None
    ),
    (
        {
            "name": " A Aaa "
        },201, None
    ),
    (
        {
            "name": "123"
        },201,None
    ),
    (
        {

        },400,"No se han aprobado todos los parámetros requeridos"
    ),
    (
        {
            "name": 123
        },400, "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"
    )
])
def test_create_kit_by_user(body, expected_status, error_message):
    toke = create_new_user(data.user.copy())
    response = create_kit_by_user(body, toke.json()["authToken"])

    assert response.status_code == expected_status

    if expected_status == 201:
        assert body["name"] == response.json()["name"]

    if expected_status == 400:
        assert error_message in response.json()["message"]


