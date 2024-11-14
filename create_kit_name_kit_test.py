import pytest
from sender_stand_request import post_new_client_kit
from data import kit_bodies

# Pruebas positivas
def positive_assert(kit_body):
    response = post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Pruebas negativas
def negative_assert_code_400(kit_body):
    response = post_new_client_kit(kit_body)
    assert response.status_code == 400

# Test 1: Validar el campo "name" con 1 carácter
def test_valid_name_1():
    positive_assert(kit_bodies["too_short"])

# Test 2: Validar el campo "name" con 511 caracteres
def test_valid_name_511():
    positive_assert(kit_bodies["valid"])

# Test 3: Validar el campo "name" vacío (debería fallar)
def test_empty_name():
    negative_assert_code_400(kit_bodies["empty"])

# Test 4: Validar el campo "name" con más de 512 caracteres (debería fallar)
def test_name_too_long():
    negative_assert_code_400(kit_bodies["too_long"])

# Test 5: Validar caracteres especiales
def test_special_characters():
    positive_assert(kit_bodies["special_chars"])

# Test 6: Validar espacios
def test_spaces_in_name():
    positive_assert(kit_bodies["with_spaces"])

# Test 7: Validar números
def test_numbers_in_name():
    positive_assert(kit_bodies["with_numbers"])

# Test 8: Si no se pasa el "name" en la solicitud, debería fallar
def test_no_name():
    negative_assert_code_400(kit_bodies["no_name"])
    
# Test 9: Si se pasa un tipo incorrecto para "name", debería fallar
def test_invalid_type_name():
    negative_assert_code_400(kit_bodies["invalid_kit"])
