import requests
from endpoints import Endpoints

class ArchivoController():

    def send_request(url, payload):
        response = requests.post(url=url, params=payload)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def crear(self, name, body, path, type):
        payload = {name, body, path, type}
        return self.send_request(Endpoints.CREAR, payload=payload)

    def delete(self, path, name, type):
        payload = {path, name, type}
        return self.send_request(Endpoints.DELETE, payload=payload)
        
    def copy(self, _from, to, type_to, type_from):
        payload = { _from, to, type_to, type_from}
        return self.send_request(Endpoints.COPY, payload=payload)
        
    def transfer(self, _from, to, type_to, type_from):
        payload = { _from, to, type_to, type_from}
        return self.send_request(Endpoints.TRANSFER, payload=payload)
    
    def rename(self, path, name, type):
        payload = {path, name, type}
        return self.send_request(Endpoints.RENAME, payload=payload)
    
    def modify(self, path, body, type):
        payload = {path, body, type}
        return self.send_request(Endpoints.MODIFY, payload=payload)
    
    def delete_all(self, type):
        payload = {type}
        return self.send_request(Endpoints.DELETE_ALL, payload=payload)
    
    def open(self, type, ip, port, name):
        payload = {type, ip, port, name}
        return self.send_request(Endpoints.OPEN, payload=payload)
        
    def backup(self, type_to, type_from, ip, port, name):
        payload = {type_to, type_from, ip, port, name}
        return self.send_request(Endpoints.BACKUP, payload=payload)
    
    def recovery(self,type_to, type_from, ip, port, name):
        payload = {type_to, type_from, ip, port, name}
        return self.send_request(Endpoints.RECOVERY, payload=payload)