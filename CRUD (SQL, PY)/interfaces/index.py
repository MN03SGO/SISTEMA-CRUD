from tkinter import *
import tkinter as tk
import webbrowser  # Librería para abrir URL

def abrir_github():
    webbrowser.open("https://github.com/MN03SGO")  

ventana = Tk()
ventana.title("CRUD")
ventana.geometry("800x600")  

# Intentar cargar el icono
try:
    imgICo = PhotoImage(file="img/LOG4iIni.png")
    ventana.iconphoto(False, imgICo)
except Exception as e:
    print("No se pudo cargar el icono:", e)

# Función para la barra de menú
def barra_menu(ventana):
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)
    
    # Menú "Inicio"
    menu_inicio = tk.Menu(barra_menu, tearoff=0) 
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio) 
    menu_inicio.add_command(label="Crear registro en BD")
    menu_inicio.add_command(label="Eliminar registro en BD")
    menu_inicio.add_separator()
    menu_inicio.add_command(label="Salir", command=ventana.quit)
    
    barra_menu.add_cascade(label="Configuración")  

    # Menú "Ayuda"
    menu_ayuda = tk.Menu(barra_menu, tearoff=0)
    menu_ayuda.add_command(label="GitHub", command=abrir_github)
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

barra_menu(ventana)

# ENTRADAS Y TEXTO
class MiFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.place(x=150, y=50)
        self.campo_galleta()

    def campo_galleta(self):
        ## TEXTOS
        self.label_nombre = tk.Label(self, text="Nombre: ", font=("Arial", 15, "bold"))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.label_cantidad = tk.Label(self, text="Cantidad: ", font=("Arial", 15, "bold"))
        self.label_cantidad.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.label_precio = tk.Label(self, text="Precio: ", font=("Arial", 15, "bold"))
        self.label_precio.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        ## ENTRADAS
        self.entry_nombre = tk.Entry(self, font=("Arial", 16))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.entry_cantidad = tk.Entry(self, font=("Arial", 16))
        self.entry_cantidad.grid(row=1, column=1, padx=10, pady=10)

        self.entry_precio = tk.Entry(self, font=("Arial", 16))
        self.entry_precio.grid(row=2, column=1, padx=10, pady=10)

        ## BTN GUARDAR  
        try:
            self.img_boton_guardar= PhotoImage(file="img/Guarda.png") 
        except Exception as e:
            print("No se pudo cargar la imagen del botón:", e)
            self.img_boton_guardar = None
        self.boton_guardar = tk.Button(self, text="Guardar")
        self.boton_guardar.config( font=("Arial", 12, "bold"),
                                        bg="green", fg="white",
                                        image=self.img_boton_guardar, compound="left")
        self.boton_guardar.grid(row=3, column=0, columnspan=2, pady=20, sticky="w")

        ## BTN MODIFICAR IMG 
        try:
            self.img_boton_modifi= PhotoImage(file="img/Modify.png") 
        except Exception as e:
            print("No se pudo cargar la imagen del botón:", e)
            self.img_boton_modifi = None
        self.boton_modifi = tk.Button(self, text="Guardar")
        self.boton_modifi.config(font=("Arial", 12, "bold"),
                                        bg="green", fg="white",
                                        image=self.img_boton_modifi, compound="center")
        self.boton_modifi.grid(row=4, column=0, columnspan=2, pady=20, sticky="n")


        try:
            self.img_boton_modifi= PhotoImage(file="img/Modify.png") 
        except Exception as e:
            print("No se pudo cargar la imagen del botón:", e)
            self.img_boton_modifi = None
        self.boton_modifi = tk.Button(self, text="Guardar")
        self.boton_modifi.config(font=("Arial", 12, "bold"),
                                        bg="green", fg="white",
                                        image=self.img_boton_modifi, compound="center")
        self.boton_modifi.grid(row=3, column=0, columnspan=2, pady=20, sticky="n")



# Crear el Frame
frame = MiFrame(ventana)

ventana.mainloop()
