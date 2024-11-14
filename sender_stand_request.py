import requests
from configuration import CREATE_USER_URL, CREATE_KIT_URL
from data import new_user_body
import data

# Función para crear un usuario
def create_new_user(user_body):
    response = requests.post(CREATE_USER_URL, json=new_user_body)
    if response.status_code == 201:
        return response.json()['authToken']  # Retorna el token de autenticación
    return None

# Función para crear un kit para el usuario
def post_new_client_kit(kit_body):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {create_new_user(new_user_body)}"
    
    response = requests.post(CREATE_KIT_URL, json=kit_body, headers=headers)
    return response
