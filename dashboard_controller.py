from archivo_controller import ArchivoController

class DashboardController():

    def operacion(self, operacion, parametros):
        if (operacion == 'create'):
            data = {"operacion": "create", "name": "", "body": "", "path": "", "ip": "", "port": ""}
            for parametro in parametros:
                campo_valor = parametro.split("->")
                if (campo_valor[0].lower() == "name"):
                    data['name'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "body"):
                    data['body'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "path"):
                    data['_path'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "ip"):
                    data['ip'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "port"):
                    data['port'] = campo_valor[1].strip("\"")
            print(data)
            archivo = ArchivoController()
            resultado = archivo._create(data)    
            return resultado['message']
        elif (operacion == 'delete_all'):
            data = {"operacion": "delete","ip": "", "port": ""}
            for parametro in parametros:
                campo_valor = parametro.split("->")
                if (campo_valor[0].lower() == "ip"):
                    data['ip'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "port"):
                    data['port'] = campo_valor[1].strip("\"")
            print(data)
            archivo = ArchivoController()
            resultado = archivo._delete_all(data)
            return resultado['message']
        if (operacion == 'backup'):
            data = {"operacion": "backup", "name": "", "ip_from": "", "port_from": "", "ip_to": "", "port_to": ""}
            for parametro in parametros:
                campo_valor = parametro.split("->")
                if (campo_valor[0].lower() == "name"):
                    data['name'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "ip_from"):
                    data['ip_from'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "port_from"):
                    data['port_from'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "ip_to"):
                    data['ip_to'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "port_to"):
                    data['port_to'] = campo_valor[1].strip("\"")
            print(data)
            archivo = ArchivoController()
            resultado = archivo._backup(data)
            print('resultado: ', resultado)    
            return resultado['message']
        elif (operacion == 'delete'):
            data = {"operacion": "delete","name": "", "path": "", "type": ""}
            for parametro in parametros:
                campo_valor = parametro.split("->")
                if (campo_valor[0].lower() == "name"):
                    data['name'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "path"):
                    data['path'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "type"):
                    data['type'] = campo_valor[1].strip("\"")
            print(data)
            archivo = ArchivoController()
            resultado = archivo.operacion(data)
            if (resultado == True):
                return 'Se ha eliminado ' + data['path']+data['name']
            return 'Error al eliminar ' + data['path']+data['name']
        elif (operacion == 'copy'):
            data = {"operacion": "copy","from": "", "to": "", "type_from": "", "type_to": ""}
            for parametro in parametros:
                campo_valor = parametro.split("->")
                if (campo_valor[0].lower() == "from"):
                    data['from'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "to"):
                    data['to'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "type_from"):
                    data['type_from'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "type_to"):
                    data['type_to'] = campo_valor[1].strip("\"")
            print(data)
            archivo = ArchivoController()
            resultado = archivo.operacion(data)
            if (resultado == True):
                return 'Se ha copiado de' + data['from']+ ' a ' + data['to']
            return 'Error al eliminar de' + data['from']+ ' a ' + data['to']
        elif (operacion == 'transfer'):
            data = {"operacion": "transfer","from": "", "to": "", "type_from": "", "type_to": ""}
            for parametro in parametros:
                campo_valor = parametro.split("->")
                if (campo_valor[0].lower() == "from"):
                    data['from'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "to"):
                    data['to'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "type_from"):
                    data['type_from'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "type_to"):
                    data['type_to'] = campo_valor[1].strip("\"")
            print(data)
            archivo = ArchivoController()
            resultado = archivo.operacion(data)
            if (resultado == True):
                return 'Se ha transferido de' + data['from']+ ' a ' + data['to']
            return 'Error al transferir de' + data['from']+ ' a ' + data['to']
        elif (operacion == 'rename'):
            data = {"operacion": "rename","path": "", "name": "", "type": ""}
            for parametro in parametros:
                campo_valor = parametro.split("->")
                if (campo_valor[0].lower() == "path"):
                    data['path'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "name"):
                    data['name'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "type"):
                    data['type'] = campo_valor[1].strip("\"")
            print(data)
            archivo = ArchivoController()
            resultado = archivo.operacion(data)
            if (resultado == True):
                return 'Se ha renombrado de' + data['path'] + ' a ' + data['name']
            return 'Error al renombrar de' + data['path']+ ' a ' + data['name']
        elif (operacion == 'modify'):
            data = {"operacion": "modify","path": "", "body": "", "type": ""}
            for parametro in parametros:
                campo_valor = parametro.split("->")
                if (campo_valor[0].lower() == "path"):
                    data['path'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "body"):
                    data['body'] = campo_valor[1].strip("\"")
                if (campo_valor[0].lower() == "type"):
                    data['type'] = campo_valor[1].strip("\"")
            print(data)
            archivo = ArchivoController()
            resultado = archivo.operacion(data)
            if (resultado == True):
                return 'Se ha modificar ' + data['path']
            return 'Error al modificar ' + data['path']
        #elif (operacion == 'backup'):
        #elif (operacion == 'recovery'):
        #elif (operacion == 'delete_all'):
        #elif (operacion == 'open'):
        else:
            return 'No se reconoce esta operacion'
