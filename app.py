from flask import Flask, request, jsonify
from usuario import Usuario
from archivo import Archivo
from bucket import Bucket

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print('data: ', str(data))
    usuario = Usuario()
    usuario_encontrado = usuario.buscar_usuario(data['username'], data['password'])
    if (usuario_encontrado is not None):
        response = {
            'message': 'Usuario encontrado',
            'data': True
        }
        return jsonify(response), 200
    return jsonify({}), 400


@app.route('/operacion', methods=['POST'])
def operacion():
    data = request.get_json()
    print('operacion data: ', str(data))
    
    if (data['operacion'] == 'create'):
        if (data['type'] == 'server'):
            archivo = Archivo()
            respuesta = archivo.crear(data['name'], data['body'], data['path'])
        else:
            bucket = Bucket()
            respuesta = bucket.crear(data['name'], data['body'], data['path'])
        if (respuesta is True):
            return jsonify({}), 200
    
    if (data['operacion'] == 'delete'):
        respuesta = archivo.delete(data['path'], data['name'], data['type'])
        if (respuesta is True):
            return jsonify({}), 200
        
    if (data['operacion'] == 'copy'):
        respuesta = archivo.copy(data['from'], data['to'], data['type_to'], data['type_from'])
        if (respuesta is True):
            return jsonify({}), 200
    
    if (data['operacion'] == 'transfer'):
        respuesta = archivo.transfer(data['from'], data['to'], data['type_to'], data['type_from'])
        if (respuesta is True):
            return jsonify({}), 200
    
    if (data['operacion'] == 'rename'):
        respuesta = archivo.rename(data['path'], data['name'], data['type'])
        if (respuesta is True):
            return jsonify({}), 200
    
    if (data['operacion'] == 'modify'):
        respuesta = archivo.modify(data['path'], data['body'], data['type'])
        if (respuesta is True):
            return jsonify({}), 200
        
    if (data['operacion'] == 'delete_all'):
        respuesta = archivo.delete_all(data['type'])
        if (respuesta is True):
            return jsonify({}), 200
        
    
    return jsonify({}), 400


@app.route('/open', methods=['POST'])
def open():
    data = request.get_json()
    print('open data: ', str(data))
    archivo = Archivo()
    respuesta = archivo.open(data['type'], data['ip'],data['port'],data['name'])
    if (respuesta is not None):
        return jsonify({}), 200
    return jsonify({}), 400

@app.route('/backup', methods=['POST'])
def backup():
    data = request.get_json()
    print('backup data: ', str(data))
    archivo = Archivo()
    respuesta = archivo.backup(data['type_to'], data['type_from'],data['ip'],data['port'],data['name'])
    if (respuesta is not None):
        return jsonify({}), 200
    return jsonify({}), 400

@app.route('/recovery', methods=['POST'])
def recovery():
    data = request.get_json()
    print('recovery data: ', str(data))
    archivo = Archivo()
    respuesta = archivo.recovery(data['type_to'], data['type_from'],data['ip'],data['port'],data['name'])
    if (respuesta is not None):
        response = {
            'message': 'Archivo creado exitosamente',
            'data': True
        }
        return jsonify(response), 200
    return jsonify({}), 400