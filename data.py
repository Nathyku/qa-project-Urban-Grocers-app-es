new_user_body = {
    "username": "newuser",
    "password": "password123",
    "email": "user@example.com"
}

# Cuerpos para crear un kit
kit_bodies = {
    "valid": {"name": "A valid kit"},
    "too_short": {"name": "a"},
    "too_long": {"name": "A" * 512},
    "empty": {"name": ""},
    "special_chars": {"name": "Kit №%@,"},
    "with_spaces": {"name": " A Aaa "},
    "with_numbers": {"name": "123"}
}