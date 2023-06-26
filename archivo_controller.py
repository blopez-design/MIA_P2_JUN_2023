import requests
from endpoints import Endpoints

class ArchivoController():
    def crear(name, body, path, type):
        return True
        response = requests.get(Endpoints.ROOT + Endpoints.LOGIN, params=None)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def delete(path, name, type):
        return True
        response = requests.get(Endpoints.ROOT + Endpoints.LOGIN, params=None)
        if response.status_code == 200:
            return True
        else:
            return False
        
    def copy(_from, to, type_to, type_from):
        return True
        response = requests.get(Endpoints.ROOT + Endpoints.LOGIN, params=None)
        if response.status_code == 200:
            return True
        else:
            return False
        
    def transfer(_from, to, type_to, type_from):
        return True
        response = requests.get(Endpoints.ROOT + Endpoints.LOGIN, params=None)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def rename(path, name, type):
        return True
        response = requests.get(Endpoints.ROOT + Endpoints.LOGIN, params=None)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def modify(path, body, type):
        return True
        response = requests.get(Endpoints.ROOT + Endpoints.LOGIN, params=None)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def delete_all(type):
        return True
        response = requests.get(Endpoints.ROOT + Endpoints.LOGIN, params=None)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def open(type, ip, port, name):
        return True
        response = requests.get(Endpoints.ROOT + Endpoints.LOGIN, params=None)
        if response.status_code == 200:
            return True
        else:
            return False
        
    def backup(type_to, type_from, ip, port, name):
        return True
        response = requests.get(Endpoints.ROOT + Endpoints.LOGIN, params=None)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def recovery(type_to, type_from, ip, port, name):
        return True
        response = requests.get(Endpoints.ROOT + Endpoints.LOGIN, params=None)
        if response.status_code == 200:
            return True
        else:
            return False