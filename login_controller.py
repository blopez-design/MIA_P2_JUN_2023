import requests
from endpoints import Endpoints

class LoginController():
    def login(a, b):
        return True
        response = requests.get(Endpoints.ROOT + Endpoints.LOGIN, params=None)
        if response.status_code == 200:
            return True
        else:
            return False
