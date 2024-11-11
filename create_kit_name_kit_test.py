import pytest
from sender_stand_request import create_new_user, post_new_client_kit
from data import kit_bodies

# Función para obtener un token de usuario
@pytest.fixture
def auth_token():
    user_body = {
        "username": "newuser",
        "password": "password123",
        "email": "user@example.com"
    }
    token = create_new_user(user_body)
    return token

# Pruebas positivas
def positive_assert(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Pruebas negativas
def negative_assert_code_400(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# Test 1: Validar el campo "name" con 1 carácter
def test_valid_name_1(auth_token):
    positive_assert(kit_bodies["too_short"], auth_token)

# Test 2: Validar el campo "name" con 511 caracteres
def test_valid_name_511(auth_token):
    positive_assert(kit_bodies["valid"], auth_token)

# Test 3: Validar el campo "name" vacío (debería fallar)
def test_empty_name(auth_token):
    negative_assert_code_400(kit_bodies["empty"], auth_token)

# Test 4: Validar el campo "name" con más de 512 caracteres (debería fallar)
def test_name_too_long(auth_token):
    negative_assert_code_400(kit_bodies["too_long"], auth_token)

# Test 5: Validar caracteres especiales
def test_special_characters(auth_token):
    positive_assert(kit_bodies["special_chars"], auth_token)

# Test 6: Validar espacios
def test_spaces_in_name(auth_token):
    positive_assert(kit_bodies["with_spaces"], auth_token)

# Test 7: Validar números
def test_numbers_in_name(auth_token):
    positive_assert(kit_bodies["with_numbers"], auth_token)

# Test 8: Si no se pasa el "name" en la solicitud, debería fallar
def test_no_name(auth_token):
    negative_assert_code_400({}, auth_token)

# Test 9: Si se pasa un tipo incorrecto para "name", debería fallar
def test_invalid_type_name(auth_token):
    invalid_kit = {"name": 123}
    negative_assert_code_400(invalid_kit, auth_token)