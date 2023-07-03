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
ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
pos_x = int(ancho_pantalla / 2 - 600 / 2)  # 200 es el ancho deseado de la ventana
pos_y = int(alto_pantalla / 2 - 400 / 2)  # 300 es el alto deseado de la ventana

# Establecer las coordenadas y el tamaño de la ventana
ventana_principal.geometry(f"600x400+{pos_x}+{pos_y}")


etiqueta_usuario = tk.Label(ventana_principal, text="Usuario:")
etiqueta_usuario.pack(pady=10)
entrada_usuario = tk.Entry(ventana_principal)
entrada_usuario.pack()

etiqueta_contraseña = tk.Label(ventana_principal, text="Contraseña:")
etiqueta_contraseña.pack(pady=10)
entrada_contraseña = tk.Entry(ventana_principal, show="*")
entrada_contraseña.pack()

boton_acceso = tk.Button(ventana_principal, text="Iniciar Sesión", command=validar_acceso)
boton_acceso.pack(pady=30)

ventana_principal.mainloop()
