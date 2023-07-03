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

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    print('operacion data: ', str(data))
    
    archivo = Archivo()
    respuesta = archivo._crear(data['name'], data['body'], data['_path'], data['ip'], data['port'])
    return jsonify(respuesta), 200

@app.route('/delete_all', methods=['POST'])
def delete_all():
    data = request.get_json()
    print('operacion data: ', str(data))
    
    archivo = Archivo()
    respuesta = archivo.delete_all(data['ip'], data['port'])
    return jsonify(respuesta), 200

@app.route('/backup', methods=['POST'])
def backup():
    data = request.get_json()
    print('operacion data: ', str(data))
    try:
        print('data bk: ',data['data'])
    except:
        data['data'] = ''
    archivo = Archivo()
    respuesta = archivo.backup_decide(data['name'], data['ip_from'], data['port_from'], data['ip_to'], data['port_to'], data['data'], data['operacion'])
    return jsonify(respuesta), 200


@app.route('/operacion', methods=['POST'])
def operacion():
    data = request.get_json()
    print('operacion data: ', str(data))
    
    if (data['operacion'] == 'create'):
        respuesta = False
        if (data['type'] == 'server'):
            archivo = Archivo()
            respuesta = archivo.crear(data['name'], data['body'], data['path'])
        elif (data['type'] == 'bucket'):
            bucket = Bucket()
            respuesta = bucket.crear(data['name'], data['body'], data['path'])
        
        if (respuesta is True):
            return jsonify({}), 200
    
    if (data['operacion'] == 'delete'):
        if (data['type'] == 'server'):
            archivo = Archivo()
            respuesta = archivo.delete(data['path'], data['name'], data['type'])
        elif (data['type'] == 'bucket'):
            bucket = Bucket()
            respuesta = bucket.eliminar(data['path'], data['name'])
        if (respuesta is True):
            return jsonify({}), 200
        
    if (data['operacion'] == 'copy'):
        respuesta = False
        if (data['type_to'] == 'server'):
            archivo = Archivo()
            respuesta = archivo.transfer(data['from'], data['to'], False)
        elif (data['type_to'] == 'bucket'):
            bucket = Bucket()
            respuesta = bucket.transfer(data['to'], data['from'])
        
        if (respuesta is True):
            return jsonify({}), 200

    if (data['operacion'] == 'transfer'):
        respuesta = False
        if (data['type_to'] == 'server'):
            archivo = Archivo()
            respuesta = archivo.transfer(data['from'], data['to'], True)
        elif (data['type_to'] == 'bucket'):
            bucket = Bucket()
            respuesta = bucket.transfer(data['to'], data['from'])
        if (respuesta is True):
            return jsonify({}), 200
        
    if (data['operacion'] == 'rename'):
        respuesta = False
        if (data['type'] == 'server'):
            archivo = Archivo()
            respuesta = archivo.rename(data['path'], data['name'])
        elif (data['type'] == 'bucket'):
            bucket = Bucket()
            respuesta = bucket.rename(data['path'], data['name'])
        
        if (respuesta is True):
            return jsonify({}), 200
    
    if (data['operacion'] == 'modify'):
        respuesta = archivo.modify(data['path'], data['body'], data['type'])
        if (respuesta is True):
            return jsonify({}), 200
        
    if (data['operacion'] == 'delete_all'):
        respuesta = False
        if (data['type'] == 'server'):
            archivo = Archivo()
            respuesta = archivo.delete_all(data['path'], data['name'], data['type'])
        elif (data['type'] == 'bucket'):
            bucket = Bucket()
            respuesta = bucket.eliminar(data['path'], data['name'])
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

""" @app.route('/backup', methods=['POST'])
def backup():
    data = request.get_json()
    print('backup data: ', str(data))
    archivo = Archivo()
    respuesta = archivo.backup(data['type_to'], data['type_from'],data['ip'],data['port'],data['name'])
    if (respuesta is not None):
        return jsonify({}), 200
    return jsonify({}), 400 """

