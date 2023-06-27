from flask import Flask, request, jsonify
from usuario import Usuario

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