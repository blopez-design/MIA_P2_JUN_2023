import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from dashboard_controller import DashboardController

class Dashboard:
    def __init__(self, root):
        self.window = tk.Tk()
        self.window.title("Dashboard")        
        self.create_widgets()
        
    def create_widgets(self):
        file_frame = tk.Frame(self.window)
        file_frame.pack(anchor="center")
        
        file_button = tk.Button(file_frame, text="Carga una archivo", command=self.open_file)
        file_button.pack(side=tk.LEFT, padx=5)
        command_frame_top = tk.Frame(file_frame)
        command_frame_top.pack(anchor="w")

        self.output_text = ScrolledText(self.window, height=20, bg="black", fg="white", wrap="none")
        self.output_text.pack(anchor="w", padx=5)
        self.output_text.configure(font=("Courier", 10))  # Configurar la fuente monoespaciada
        self.output_text.tag_configure("code", font=("Courier", 10))  # Configurar el estilo de la sintaxis
        self.output_text.bind("<Return>", self.execute_command)

        output_label_bottom = tk.Label(self.window, text="Salida inferior:")
        output_label_bottom.pack(anchor="w")
        self.output_text_bottom = tk.Text(self.window, height=5)
        self.output_text_bottom.pack(padx=5)
        
    def open_file(self):
        file_path = filedialog.askopenfilename()
        self.leer_archivo(file_path)

    
    def ejecutar(self, operacion, parametros):
        resultado = ''
        dashboard_controller = DashboardController()
        print(operacion.lower(), str(parametros))
        resultado = dashboard_controller.operacion(operacion.lower(), parametros)
        self.output_text_bottom.insert(tk.END, resultado + '\n')
        self.output_text_bottom.update()


    def leer_archivo(self, ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                self.output_text.insert(tk.END, linea)
                self.output_text.update()
                linea = linea.rstrip('\n')
                parametros = linea.split(" -")
                self.ejecutar(parametros[0], parametros[1:])

    def execute_command(self, event=None):
        command = self.output_text.get("1.0", tk.END)
        commands = command.splitlines()
        ultimo = commands[-1]
        if (ultimo == "clear"):
            self.output_text.delete("1.0", tk.END)
            self.output_text_bottom.delete("1.0", tk.END)
            return
        command = command.rstrip('\n')
        parametros = command.split(" -")
        self.ejecutar(parametros[0], parametros[1:])

    def run(self):
        self.window.mainloop()



