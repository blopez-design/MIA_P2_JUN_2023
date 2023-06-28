import os
import shutil

class Archivo:
    
    root = './archivos'
    
    def crear(self, name, body, path, type):
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

        
    def copy(self, _from, to, type_to, type_from):
        _from = self.root + _from
        to = self.root + to
        try:
            if os.path.isfile(_from):
                shutil.copy(_from, to)
                print(f"Se copió el archivo: {_from} -> {to}")
                return True
            else:
                # Si no se proporcionó el nombre del archivo en la ruta de origen, copiar toda la carpeta
                if not os.path.basename(_from):
                    shutil.copytree(_from, to)
                    print(f"Se copió la carpeta y su contenido: {_from} -> {to}")
                    return True
                else:
                    print("No se proporcionó un nombre de archivo válido.")
                    return False
        except Exception as e:
            print(f"Error al eliminar la ruta: {e}")
            return False
        
    def transfer(self, _from, to, type_to, type_from):
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
            return False
        
    
    def rename(self, path, name, type):
        path = self.ro + path
        try:
            directorio_padre = os.path.dirname(path)
            extension = os.path.splitext(path)[1]
            nueva_ruta = os.path.join(directorio_padre, name + extension)
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
        
    
    def modify(self, path, body, type):
        path = self.root + path
        try:
            with open(path, 'w') as archivo:
                archivo.write(body)
            print("El contenido del archivo se ha modificado correctamente.")
            return True
        except Exception:
            print(f"No se pudo modificar el archivo: {path}")
            return False
    
    def delete_all(self, type):
        try:
            for archivo in os.listdir(self.root):
                ruta_archivo = os.path.join(self.root, archivo)
                if os.path.isfile(ruta_archivo):
                    os.remove(ruta_archivo)
                    print(f"Se eliminó el archivo: {ruta_archivo}")
                else:
                    shutil.rmtree(ruta_archivo)
        except Exception as e:
            print(f"Error al eliminar todos los archivos")
            return False
        
    def open(self, type, ip, port, name):
        payload = {type, ip, port, name}
        return self.send_request(Endpoints.OPEN, payload=payload)
        
    def backup(self, type_to, type_from, ip, port, name):
        payload = {type_to, type_from, ip, port, name}
        return self.send_request(Endpoints.BACKUP, payload=payload)
    
    def recovery(self,type_to, type_from, ip, port, name):
        payload = {type_to, type_from, ip, port, name}
        return self.send_request(Endpoints.RECOVERY, payload=payload)
