import os
BASE_URL = os.getenv("BASE_URL", "https://cnt-752fe526-b7b2-4378-aa43-bce4348d87c8.containerhub.tripleten-services.com")
CREATE_USER_URL = f"{BASE_URL}/api/v1/users"
CREATE_KIT_URL = f"{BASE_URL}/api/v1/kits"