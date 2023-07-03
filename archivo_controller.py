import requests
import endpoints as end
import json

class ArchivoController():

    def send_request(self, url, data):
        headers = {"Content-Type": "application/json"}
        print(url, data, headers)
        json_data = json.dumps(data)
        response = requests.post(url=url, headers=headers, data=json_data)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def _send_request(self, url, data):
        headers = {"Content-Type": "application/json"}
        print(url, data, headers)
        json_data = json.dumps(data)
        try:
            response = requests.post(url=url, headers=headers, data=json_data)
            print('Respuesta: ', response)
            return response.json()
        except Exception as e:
            return {"status": False, "message": 'Error en la solcitud: ' + str(e)}
    
    def _create(self, data):
        url = f'http://{data["ip"]}:{data["port"]}/create'
        return self._send_request(url, data=data)
    
    def _delete_all(self, data):
        url = f'http://{data["ip"]}:{data["port"]}/delete_all'
        return self._send_request(url, data=data)
    

    def _backup(self, data):
        url_from = f'http://{data["ip_from"]}:{data["port_from"]}/backup'
        return self._send_request(url_from, data=data)
    

    def operacion(self, data):
        return self.send_request(end.OPERACION, data=data)

    def open(self, type, ip, port, name):
        payload = {type, ip, port, name}
        return self.send_request(end.OPEN, payload=payload)
        
    def backup(self, type_to, type_from, ip, port, name):
        payload = {type_to, type_from, ip, port, name}
        return self.send_request(end.BACKUP, payload=payload)
    
    def recovery(self,type_to, type_from, ip, port, name):
        payload = {type_to, type_from, ip, port, name}
        return self.send_request(end.RECOVERY, payload=payload)