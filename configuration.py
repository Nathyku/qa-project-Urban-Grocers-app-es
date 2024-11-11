import os
BASE_URL = os.getenv("BASE_URL", "https://cnt-180d68b3-a6f9-4321-adf4-efe331664638.containerhub.tripleten-services.com")
CREATE_USER_URL = f"{BASE_URL}/api/v1/users"
CREATE_KIT_URL = f"{BASE_URL}/api/v1/kits"