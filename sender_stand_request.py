import requests
from configuration import CREATE_USER_URL, CREATE_KIT_URL
from data import new_user_body, kit_bodies

# Función para crear un usuario
def create_new_user(user_body):
    response = requests.post(CREATE_USER_URL, json=user_body)
    if response.status_code == 201:
        return response.json()['authToken']  # Retorna el token de autenticación
    return None

# Función para crear un kit para el usuario
def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    
    response = requests.post(CREATE_KIT_URL, json=kit_body, headers=headers)
    return response
