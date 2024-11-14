import os
BASE_URL = os.getenv("BASE_URL", "https://cnt-7bf1dd38-50b8-46ee-8b14-43fd133988f0.containerhub.tripleten-services.com")
CREATE_USER_URL = f"{BASE_URL}/api/v1/users"
CREATE_KIT_URL = f"{BASE_URL}/api/v1/kits"