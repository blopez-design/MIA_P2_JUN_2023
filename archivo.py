import os
import shutil
import json
import socket
import requests

class Archivo:
    
    backup = './backup/'
    root = './archivos'
    recovery = '/recovery'
    nombre_host = socket.gethostname()
    direccion_ip = socket.gethostbyname(nombre_host)

    def _delete_all(self, ip, port):
        try:
            shutil.rmtree(self.root)
            os.mkdir(self.root)
            return {"status": True, "message": f'El servidor http://{ip}:{port} esta vacío.'}
        except Exception as e:
            return {"status": False, "message": f'Error al eliminar archivos del servidor http://{ip}:{port}. Razón: ${e}'}


    def _crear(self, name, body, path, ip, port):
        temp_path = self.root + path
        path = self.root + path + name
        try:
            print(temp_path)
            if os.path.exists(temp_path):
                print('path existe', name)
                if(name == ""):
                    return {"status": False, "message": f'La carpeta {temp_path.replace("./archivos", "")} ya existe en http://{ip}:{port}.'}            

            if os.path.exists(path):
                base_path, name = os.path.split(path)
                name, ext = os.path.splitext(name)
        
                count = 1
                while os.path.exists(os.path.join(base_path, f"{name}_{count}{ext}")):
                    count += 1
        
                name = f"{name}_{count}"
                path = os.path.join(base_path, name + ext)
        
            carpetas, archivo = os.path.split(path)
        
            if carpetas:
                os.makedirs(carpetas, exist_ok=True)
            
            if body:
                with open(path, 'w') as file:
                    file.write(body)
            else:
                if archivo:
                    open(path, 'a').close()
            return {"status": True, "message": f'El objecto {path.replace("./archivos", "")} ha sido creado en http://{ip}:{port}.'}
        except Exception as e:
            return {"status": False, "message": f'Error al crear objecto {path.replace("./archivos", "")} en http://{ip}:{port}. Razón: {e.message}'}
        


    def recoveryReceive(self):# here<--------------------
        if self.tipoDe == "server":
            res = requests.post(
                url=f"http://{self.ip}:{self.port}/recoveryg",  #URL METODO
                json={"type_to": self.tipoA, "type_from": self.tipoDe,
                      "name": self.name, "archivos": self.archivos}  #LO QUE ENVIO
            )
            jsoN=json.loads(res.text)
            if self.tipoA == "server":
                self.recorrerJsonServer(f'./{self.name}',jsoN["data"]["archivos"],self.tipoA,self.name) #original
            elif self.tipoA == "bucket":
                self.recorrerJsonServer(f'{self.name}/', jsoN["data"]["archivos"], self.tipoA, self.name)
            return res.text
        
    def backup_decide(self, name, ip_from, port_from, ip_to = "", port_to = "", data = "", operacion = ""):
        if (ip_to == "" and port_to == ""):
            return self.backup_local(ip_from, port_from, name, operacion)
        elif (ip_to != "" and port_to != ""):
            return self.backup_clud(ip_to, port_to, name, ip_from, port_from, data, operacion)
        else:
            return {"status": False, "message": f'Error se desconce donde necesita realizar el {operacion}'}

    def backup_local(self, ip_from, port_from, name, operacion):
        try:
            if (operacion == 'backup'):
                shutil.copytree(self.root, self.backup+name)
                return {"status": True, "message": f'{operacion} en {ip_from}:{port_from} creado exitosamente'}
            else:
                if os.path.exists(self.backup+name):
                    shutil.copytree(self.backup + name, self.root + self.recovery)
                    return {"status": True, "message": f'{operacion} en {ip_from}:{port_from} creado exitosamente'}         
                else:
                    return {"status": False, "message": f'El {operacion} en {ip_from}:{port_from} no existe'}
        except Exception as e:
            return {"status": False, "message": f'Error al crear {operacion} en {ip_from}:{port_from}. Razón: {e}'}

    def backup_clud(self, ip_to, port_to, name, ip_from, port_from, data, operacion):
            if (data == ""):
                try:
                    ruta = self.root
                    if (operacion == 'recovery'):
                        ruta = self.backup + name
                    if os.path.exists(ruta):
                        resT = self.listadoJsonServer(ruta)
                        response = requests.post(url=f"http://{ip_to}:{port_to}/backup", 
                                                json={"ip_from": ip_from, "port_from": port_from, "ip_to": ip_to, "port_to": port_to, "name": name, "data": json.loads("{"+resT+"}")})
                        return response.json()
                    else:
                        return {"status": False, "message": f'El {operacion} en {ip_from}:{port_from} no existe'}
                except Exception as e:
                    return {"status": False, "message": f'Error al conectarse con {ip_to}:{port_to}. Razón: {e}'}
            else:
                try:
                    ruta = self.backup+name
                    if (operacion == 'recovery'):
                        ruta = self.root + self.recovery
                    self.recorrerJsonServer(ruta, data)
                    return {"status": True, "message": f'{operacion} en {ip_to}:{port_to} creado exitosamente'}
                except Exception as e:
                    return {"status": False, "message": f'Error al realizar {operacion} en {ip_to}:{port_to}. Razón: {e}'}

    def listadoJsonServer(self, url):
        listado = os.listdir(url)
        txtJson = ''
        for iI in range(len(listado)):
            if '.txt' in listado[iI]:  # es archivo
                if iI < len(listado)-1:  # ultimo item
                    txtJson += '"'+listado[iI]+'":"' + \
                        self.readTxt(os.path.join(url, listado[iI]))+'",'
                else:
                    txtJson += '"'+listado[iI]+'":"' + \
                        self.readTxt(os.path.join(url, listado[iI]))+'"'
                    return txtJson
            else:  # es carpeta
                if iI < len(listado)-1:  # ultimo item
                    txtJson += '"' + \
                        listado[iI] + \
                        '":{'+self.listadoJsonServer(os.path.join(url, listado[iI]))+'},'
                else:
                    txtJson += '"' + \
                        listado[iI] + \
                        '":{'+self.listadoJsonServer(os.path.join(url, listado[iI]))+'}'
                    return txtJson
        return ''

    def readTxt(self, path):
        contenido = ''
        try:
            with open(path, 'r') as archivo:
                contenido = archivo.read()
            return contenido
        except Exception as e:
            return e

    def recorrerJsonServer(self, ruta, aJson):
        for aA in aJson:  # NORMAL
            print('elemento: ' + aA)
            if '.txt' in aA:  # txt
                self.screateSever(aA, aJson[aA], ruta+'/')
            else:  # folder
                os.makedirs(f'{ruta}/{aA}', exist_ok=True)  # creo por si no existe
                self.recorrerJsonServer(f'{ruta}/{aA}', aJson[aA])
    
    def screateSever(self, nombre, contenido, path):
        with open(path+nombre, 'w') as archivo:
            if contenido is not None:
                archivo.write(contenido)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def crear(self, name, body, path):
        path = self.root + path + name
        try:
            if os.path.exists(path):
                base_path, name = os.path.split(path)
                name, ext = os.path.splitext(name)
        
                count = 1
                while os.path.exists(os.path.join(base_path, f"{name}_{count}{ext}")):
                    count += 1
        
                name = f"{name}_{count}"
                path = os.path.join(base_path, name + ext)
        
            carpetas, archivo = os.path.split(path)
        
            if carpetas:
                os.makedirs(carpetas, exist_ok=True)
            
            if body:
                with open(path, 'w') as file:
                    file.write(body)
            else:
                if archivo:
                    open(path, 'a').close()
            return True
        
        except Exception as e:
            print(f"Error al crear la ruta: {e}")
            return False

    def delete(self, path, name, type):
        ruta = self.root + path + name
        try:
            if os.path.isfile(ruta):
                os.remove(ruta)
                print(f"Se eliminó el archivo: {ruta}")
            else:
                shutil.rmtree(ruta)
                return True
        except Exception as e:
            print(f"Error al eliminar la ruta: {e}")
            return False

        
    def copy(self, _from, to):
        return self.transfer(_from, to, False)
        
    def transfer(self, path_origen, path_destino, is_transfer = True):
        path_origen = self.root + path_origen
        path_destino = self.root + path_destino
        print('hola1', path_origen)
        print('hola2', path_destino)
        carpetas, archivo = os.path.split(path_origen)
        try:
            if archivo:
                print('es archivo')
                self.transferir_archivo_individual(path_origen, path_destino)
                self.eliminar_archivo(path_origen, is_transfer)
            elif carpetas:
                self.transferir_carpeta_completa(path_origen, path_destino, is_transfer)
            return True
        except Exception as e:
            print(f"Error al eliminar la ruta: {e}")
            return False

    def transferir_archivo_individual(self, path_origen, path_destino):
        nombre_archivo, extension = os.path.basename(path_origen).split(".")
        archivo_destino = os.path.join(path_destino, os.path.basename(path_origen))
        if os.path.exists(archivo_destino):
            identificador = 1
            while os.path.exists(f"{path_destino}/{nombre_archivo}_{identificador}.{extension}"):
                identificador += 1
            nuevo_nombre = f"{nombre_archivo}_{identificador}.{extension}"
            archivo_destino = os.path.join(path_destino, nuevo_nombre)
        shutil.copy2(path_origen, archivo_destino)
        print(f"Archivo transferido: {archivo_destino}")

    def transferir_carpeta_completa(self, path_origen, path_destino, is_transfer):
        if not os.path.exists(path_destino):
            os.makedirs(path_destino)

        for root, _, files in os.walk(path_origen):
            for file in files:
                path_archivo_origen = os.path.join(root, file)
                path_archivo_destino = os.path.join(path_destino, file)
                self.transferir_archivo_individual(path_archivo_origen, path_archivo_destino, is_transfer)
                self.eliminar_archivo(path_archivo_origen, is_transfer)
        
    def eliminar_archivo(self, path_archivo, is_transfer):
        if is_transfer is True:
            os.remove(path_archivo)
        print(f"Archivo eliminado: {path_archivo}")
        
    """ def transfer(self, _from, to):
        _from = self.root + _from
        to = self.root + to
        try:
            if shutil.os.path.isfile(_from):
                shutil.move(_from, to)
                print(f"Se transfirió el archivo: {_from} -> {to}")
            else:
                shutil.move(_from, to)
                print(f"Se transfirió la carpeta y su contenido: {_from} -> {to}")
            return True
        except Exception as e:
            print(f"Error al transferir la ruta: {_from} a {to}")
            return False """
        
    
    def rename(self, path, name):
        path = self.root + path
        try:
            directorio_padre = os.path.dirname(path)
            nueva_ruta = os.path.join(directorio_padre, name)
            if os.path.exists(nueva_ruta):
                print(f"Ya existe un archivo con el nombre {name}.")
                return False
            else:
                os.rename(path, nueva_ruta)
                print(f"El archivo se ha renombrado correctamente a: {name}")
                return True
        except Exception as e:
            print(f"Error al renombrar la ruta: {path} a {name}")
            return False
        
    
    def modify(self, path, body):
        path = self.root + path
        try:
            with open(path, 'w') as archivo:
                archivo.write(body)
            print("El contenido del archivo se ha modificado correctamente.")
            return True
        except Exception:
            print(f"No se pudo modificar el archivo: {path}")
            return False
    
    def delete_all(self, path, name, type):
        path = self.root + path + name
        try:
            for archivo in os.listdir(self.root):
                ruta_archivo = os.path.join(self.root, archivo)
                if os.path.isfile(ruta_archivo):
                    os.remove(ruta_archivo)
                    print(f"Se eliminó el archivo: {ruta_archivo}")
                else:
                    shutil.rmtree(ruta_archivo)
            return True
        except Exception as e:
            print(f"Error al eliminar todos los archivos")
            return False
        
    def open(self, type, ip, port, name):
        payload = {type, ip, port, name}
        return self.send_request(Endpoints.OPEN, payload=payload)
