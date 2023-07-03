import boto3
import os
from botocore.exceptions import ClientError

class Bucket():


    root = 'archivos'
    bucket_name = '202001574'
    """ s3_client = boto3.client('s3',
        aws_access_key_id='AKIAVB4S634UX5DBHGAC',
        aws_secret_access_key='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'
    ) """


    s3_client = boto3.client('s3',
        aws_access_key_id='AKIAYM5J3T4AQR5PCNSP',
        aws_secret_access_key='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'
    )


    
    def crear(self, name, body, path, path_to = None):
        ruta_archivo = self.root + path + name
        
        if path_to is not None:
            ruta_archivo = path_to

        nombre_archivo = os.path.basename(ruta_archivo)
        ruta_carpetas = os.path.dirname(ruta_archivo)

        s3_client = self.s3_client
        try:
            if nombre_archivo:
                if self.verificar_archivo_en_s3(self.bucket_name, ruta_carpetas, nombre_archivo):
                    identificador = self.obtener_identificador_autoincrementable(self.bucket_name, ruta_carpetas, nombre_archivo)
                    nombre_archivo_nuevo = f"{os.path.splitext(nombre_archivo)[0]}_{identificador}{os.path.splitext(nombre_archivo)[1]}"
                    key = f"{ruta_carpetas}/{nombre_archivo_nuevo}"
                    print(f"El archivo ya existe en S3. Creando archivo con nuevo nombre: {nombre_archivo_nuevo}")
                else:
                    key = f"{ruta_carpetas}/{nombre_archivo}"
                    print(f"El archivo no existe en S3. Creando archivo con nombre original: {nombre_archivo}")

                subdirectorios = ruta_carpetas.split('/')
                for i in range(1, len(subdirectorios) + 1):
                    directorio = '/'.join(subdirectorios[:i])
                    s3_client.put_object(Bucket=self.bucket_name, Key=f"{directorio}/")

                s3_client.put_object(Body=body, Bucket=self.bucket_name, Key=key)
                print(f"Se creó el archivo en S3: {key}")
            else:
                for directorio in ruta_carpetas.split('/'):
                    if directorio:
                        s3_client.put_object(Bucket=self.bucket_name, Key=f"{directorio}/")
                print(f"Se crearon las carpetas en S3: {ruta_carpetas}")
            return True
        except Exception as e:
            print(f"Error al crear la ruta: {e}")
            return False

    def verificar_archivo_en_s3(self, bucket_name, ruta_carpetas, nombre_archivo):
        s3_client = self.s3_client
        key = f"{ruta_carpetas}/{nombre_archivo}"
        try:
            s3_client.head_object(Bucket=bucket_name, Key=key)
            return True
        except:
            return False

    def obtener_identificador_autoincrementable(self, bucket_name, ruta_carpetas, nombre_archivo):
        s3_client = self.s3_client
        identificador = 1
        while True:
            nombre_archivo_nuevo = f"{os.path.splitext(nombre_archivo)[0]}_{identificador}{os.path.splitext(nombre_archivo)[1]}"
            key = f"{ruta_carpetas}/{nombre_archivo_nuevo}"
            try:
                s3_client.head_object(Bucket=bucket_name, Key=key)
                identificador += 1
            except:
                return identificador
    
    def eliminar(self, path, name):
        
        s3_client = self.s3_client

        ruta_archivo = self.root + path + name
        print(ruta_archivo)
        nombre_archivo = os.path.basename(ruta_archivo)
        ruta_carpetas = os.path.dirname(ruta_archivo)
        try:
            if nombre_archivo:
                self.s3_client.delete_object(Bucket=self.bucket_name, Key=ruta_archivo)
                print(f"Se eliminó el archivo en S3: {ruta_archivo}")
            else:
                self.s3_client.delete_object(Bucket=self.bucket_name, Key=f"{ruta_carpetas}/")
                
                print(f"Se eliminó todo el contenido de la carpeta en S3: {ruta_carpetas}")
            return True
        except Exception as e:
            print(f"Error al eliminar la ruta: {e}")
            return False

    def transfer(self, path_to, path_from):
        path_to = self.root + path_to
        path_from = self.root + path_from
        # Obtener el nombre del archivo o carpeta del path_from
        nombre_original = os.path.basename(path_from)
        ruta_carpetas = os.path.dirname(path_from)
        # Verificar si el archivo o carpeta existe en el path_to
        if self.existe_archivo_o_carpeta(path_to):
            # El archivo o carpeta ya existe en el path_to
            nombre_nuevo = self.obtener_nombre_nuevo(nombre_original, ruta_carpetas)
            path_to = f"{ruta_carpetas}/{nombre_nuevo}"
            
        # Verificar si el path_from es un archivo o carpeta
        if nombre_original:
            self.transferir_archivo(path_from, path_to)
        elif ruta_carpetas:
            self.transferir_carpeta(path_from, path_to)
        else:
            print(f"El path_from '{path_from}' no es un archivo ni una carpeta válida.")

    def transferir_archivo(self, path_from, path_to):
        # Obtener el nombre del archivo
        nombre_archivo = os.path.basename(path_from)

        # Subir el archivo al bucket de S3
        try:
            self.s3_client.upload_file(path_from, self.bucket_name, f"{path_to}/{nombre_archivo}")
            print(f"Se ha transferido el archivo a '{path_to}/{nombre_archivo}' en S3.")
        except ClientError as e:
            print(f"No se pudo transferir el archivo a S3: {e}")

    def transferir_carpeta(self, path_from, path_to):
        # Subir cada archivo dentro de la carpeta al bucket de S3 recursivamente
        for root, dirs, files in os.walk(path_from):
            for file in files:
                archivo_completo = os.path.join(root, file)
                archivo_rel_path = os.path.relpath(archivo_completo, path_from)
                s3_key = f"{path_to}/{archivo_rel_path}"
                self.transferir_archivo(archivo_completo, s3_key)
        
        print(f"Se han transferido los archivos de la carpeta a '{path_to}' en S3.")

    def existe_archivo_o_carpeta(self, path_to):
        try:
            self.s3_client.head_object(Bucket=self.bucket_name, Key=f"{path_to}")
            return True
        except ClientError:
            return False

    def obtener_nombre_nuevo(self, nombre_original, path_to):
        nombre_base, extension = os.path.splitext(nombre_original)
        contador = 1
        while True:
            nombre_nuevo = f"{nombre_base}_{contador}{extension}"
            if not self.existe_archivo_o_carpeta(path_to + nombre_nuevo):
                return nombre_nuevo
            contador += 1
    

    def rename(self, ruta_archivo, nuevo_nombre):
        ruta_archivo = self.root + ruta_archivo
        nombre_archivo = ruta_archivo.split('/')[-1]
        nueva_ruta_archivo = ruta_archivo.replace(nombre_archivo, nuevo_nombre)
        self.s3_client.copy_object(
            CopySource={'Bucket': self.bucket, 'Key': ruta_archivo},
            Bucket=self.bucket,
            Key=nueva_ruta_archivo
        )
        self.s3_client.delete_object(Bucket=self.bucket, Key=ruta_archivo)


