from Crypto.Cipher import AES
import binascii

def desencriptar_aes_ecb(cadena_encriptada, llave):
    clave = llave
    cipher = AES.new(clave.encode(), AES.MODE_ECB)
    cadena_descifrada = cipher.decrypt(binascii.unhexlify(cadena_encriptada))
    return cadena_descifrada.decode()