import os
new_user_body = {
    "username": os.getenv("DEFAULT_USERNAME", "newuser"),
    "password": os.getenv("DEFAULT_PASSWORD", "password123"),
    "email": os.getenv("DEFAULT_EMAIL", "user@example.com")
}

kit_bodies = {
    "valid": {"name": os.getenv("VALID_KIT_NAME", "A valid kit")},
    "too_short": {"name": os.getenv("TOO_SHORT_KIT_NAME", "a")},

    "too_long": {"name": os.getenv("TOO_LONG_KIT_NAME", "A" * 512)},
    "empty": {"name": os.getenv("EMPTY_KIT_NAME", "")},

    "special_chars": {"name": os.getenv("SPECIAL_CHARS_KIT_NAME", "Kit №%@,")},
    "with_spaces": {"name": os.getenv("SPACES_IN_NAME", " A Aaa ")},

    "with_numbers": {"name": os.getenv("NUMERIC_KIT_NAME", "123")},
    "invalid_kit": {"name": os.getenv("INVALID_KIT_NAME_TYPE", 123)},

    "no_name": {}  # Nuevo caso donde `name` está ausente
}