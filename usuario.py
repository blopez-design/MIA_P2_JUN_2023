import desencriptar as desencriptar

class Usuario:
    def __init__(self, usuario = None, contrasena = None):
        self.usuario = usuario
        self.contrasena = contrasena

    def buscar_usuario(self, txt_usuario, txt_contrasena):
        encontrado = None
        ruta_archivo = './calificacion/miausuarios.txt'
        usuarios = self.cargar_usuarios_desde_archivo(ruta_archivo)
        for user in usuarios:        
            user.contrasena = user.contrasena.replace("\x07", "")
            if user.usuario == txt_usuario and user.contrasena == txt_contrasena:
                encontrado = user
                break
        return encontrado

    def cargar_usuarios_desde_archivo(self, archivo):
        usuarios = []
        with open(archivo, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                usuario = lines[i].strip()
                print("Usuario:", usuario)
                contrasena = lines[i+1].strip()
                print("Contraseña:", desencriptar.desencriptar_aes_ecb(contrasena, 'miaproyecto12345'))
                usuario_obj = Usuario(usuario, desencriptar.desencriptar_aes_ecb(contrasena, 'miaproyecto12345'))
                usuarios.append(usuario_obj)
        return usuarios