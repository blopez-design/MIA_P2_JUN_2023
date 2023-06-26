class DashboardController():

    def ejecutar(operacion, parametros):
        print(operacion, str(parametros))


    def leer_archivo(self, ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.rstrip('\n')
                parametros = linea.split(" -")
                self.ejecutar(parametros[0], parametros[1:])
