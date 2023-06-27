import requests
import endpoints as end
import json

class LoginController():
    
    def login(self, username, password):
        params = {"username": username, "password": password}
        endpoint = end.LOGIN
        headers = {'Content-Type': 'application/json'}
        json_data = json.dumps(params)
        response = requests.post(endpoint, headers=headers, data=json_data)
        if response.status_code == 200:
            return True
        else:
            return False
