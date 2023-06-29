import boto3
import os

class Bucket():


    root = '.archivos/'
    bucket_name = 'mia-201602619'
    s3_client = boto3.client('s3',
        aws_access_key_id='AKIAVB4S634UX5DBHGAC',
        aws_secret_access_key='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'
    )
    
    def crear(self, name, body, path):
        ruta_archivo = self.root + path + name
        nombre_archivo = os.path.basename(ruta_archivo)
        ruta_carpetas = os.path.dirname(ruta_archivo)
        if nombre_archivo:
            self.put_object(Body=body, Bucket=self.bucket_name, Key=nombre_archivo)
            print(f"Se creó el archivo en S3: {nombre_archivo}")
        else:
            for directorio in ruta_carpetas.split('/'):
                if directorio:
                    self.s3_client.put_object(Bucket=self.bucket_name, Key=directorio+'/')
            print(f"Se crearon las carpetas en S3: {ruta_carpetas}")
