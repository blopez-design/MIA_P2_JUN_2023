import tkinter as tk
from tkinter import messagebox
from login_controller import LoginController
from dashboard import Dashboard



def validar_acceso():
    txt_usuario = entrada_usuario.get()
    txt_contrasena = entrada_contraseña.get()

    loginController = LoginController()
    usuario_encontrado = loginController.login(txt_usuario, txt_contrasena)
    
    if usuario_encontrado is True:
        messagebox.showinfo("Acceso concedido", "¡Bienvenido, admin!")
        ventana_principal.withdraw()
        ventana_dashboard = Dashboard(ventana_principal)
        ventana_dashboard.run()
    else:
        messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")
           
ventana_principal = tk.Tk()
ventana_principal.geometry("600x400")

etiqueta_usuario = tk.Label(ventana_principal, text="Usuario:")
etiqueta_usuario.pack()
entrada_usuario = tk.Entry(ventana_principal)
entrada_usuario.pack()

etiqueta_contraseña = tk.Label(ventana_principal, text="Contraseña:")
etiqueta_contraseña.pack()
entrada_contraseña = tk.Entry(ventana_principal, show="*")
entrada_contraseña.pack()

boton_acceso = tk.Button(ventana_principal, text="Acceso", command=validar_acceso)
boton_acceso.pack()

ventana_principal.mainloop()
