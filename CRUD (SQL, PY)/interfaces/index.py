from tkinter import *
import tkinter as tk
import webbrowser  
from PIL import Image, ImageTk  
from tkinter import ttk

def abrir_github():
    webbrowser.open("https://github.com/MN03SGO")  

ventana = Tk()
ventana.title("CRUD")

try:
    imgICo = PhotoImage(file="img/LOG4iIni.png")
    ventana.iconphoto(False, imgICo)
except Exception as e:
    print("No se pudo cargar el icono:", e)

def barra_menu(ventana):
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)
    
    menu_inicio = tk.Menu(barra_menu, tearoff=0) 
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio) 
    menu_inicio.add_command(label="Crear registro en BD")
    menu_inicio.add_command(label="Eliminar registro en BD")
    menu_inicio.add_separator()
    menu_inicio.add_command(label="Salir", command=ventana.quit)
    
    barra_menu.add_cascade(label="Configuración")  

    menu_ayuda = tk.Menu(barra_menu, tearoff=0)
    menu_ayuda.add_command(label="GitHub", command=abrir_github)
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

barra_menu(ventana)

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

class MiFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=0, column=0, padx=50, pady=50, sticky="nsew")
        self.columnconfigure((0, 1, 2), weight=1)
        self.campo_galleta()
        self.Des_campos()  # Desactiva los campos al inicio
        

    def campo_galleta(self):
        # Labels
        self.label_nombre = tk.Label(self, text="Nombre: ", font=("Arial", 18, "bold"))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.label_cantidad = tk.Label(self, text="Cantidad: ", font=("Arial", 18, "bold"))
        self.label_cantidad.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.label_precio = tk.Label(self, text="Precio: ", font=("Arial", 18, "bold"))
        self.label_precio.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.label_descripcion = tk.Label(self, text="Descripción: ", font=("Arial", 18, "bold"))
        self.label_descripcion.grid(row=3, column=0, padx=10, pady=10, sticky="ne")

        # Entradas de texto
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre, font=("Arial", 18), width=35)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.mi_cantidad = tk.StringVar() 
        self.entry_cantidad = tk.Entry(self, textvariable=self.mi_cantidad, font=("Arial", 18), width=35)
        self.entry_cantidad.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.mi_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable=self.mi_precio, font=("Arial", 18), width=35)
        self.entry_precio.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.mi_descripcion = tk.StringVar()
        self.entry_descripcion = tk.Entry(self, textvariable=self.mi_descripcion, font=("Arial", 18), width=35)
        self.entry_descripcion.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        def cargar_imagen(ruta):
            try:
                img = Image.open(ruta)
                img = img.resize((40, 40))  
                return ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"No se pudo cargar la imagen {ruta}:", e)
                return None
        
        self.img_boton_nuevo = cargar_imagen("img/Nuevo.png")
        self.img_boton_guardar = cargar_imagen("img/Guarda.png")
        self.img_boton_modifi = cargar_imagen("img/Modify.png")
        self.img_boton_elimi = cargar_imagen("img/Eliminar.png")

        # Frame de botones
        boton_frame = tk.Frame(self)
        boton_frame.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")
        boton_frame.columnconfigure((0, 1, 2, 3), weight=1)

        # Botón Nuevo
        self.boton_nuevo = tk.Button(boton_frame, text="Nuevo", font=("Arial", 14, "bold"),
                                    bg="green", fg="white",
                                    image=self.img_boton_nuevo, compound="left",
                                    width=170, height=60,
                                    command=self.Hab_campos)
        self.boton_nuevo.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Botón Guardar
        self.boton_guardar = tk.Button(boton_frame, text="Guardar", font=("Arial", 14, "bold"),
                                    bg="green", fg="white",
                                    image=self.img_boton_guardar, compound="left",
                                    width=170, height=60,
                                    command=self.guardar_dat)
        self.boton_guardar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Botón Modificar
        self.boton_modifi = tk.Button(boton_frame, text="Modificar", font=("Arial", 14, "bold"),
                                    bg="blue", fg="white",
                                    image=self.img_boton_modifi, compound="left",
                                    width=170, height=60,
                                    command=self.Hab_campos)
        self.boton_modifi.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # Botón Eliminar
        self.boton_eliminar = tk.Button(boton_frame, text="Eliminar", font=("Arial", 14, "bold"),
                                        bg="red", fg="white",
                                        image=self.img_boton_elimi, compound="left",
                                        width=170, height=60,
                                        command=self.Des_campos)
        self.boton_eliminar.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    def Hab_campos(self):
        """Habilita los campos de entrada"""
        self.entry_nombre.config(state="normal")
        self.entry_cantidad.config(state="normal")
        self.entry_precio.config(state="normal")
        self.entry_descripcion.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_modifi.config(state="disabled")
        self.boton_eliminar.config(state="normal")

    def Des_campos(self):
        """Deshabilita los campos y limpia los valores"""
        self.mi_nombre.set("")
        self.mi_cantidad.set("")
        self.mi_precio.set("")
        self.mi_descripcion.set("")

        self.entry_nombre.config(state="disabled")
        self.entry_cantidad.config(state="disabled")
        self.entry_precio.config(state="disabled")
        self.entry_descripcion.config(state="disabled")

        self.boton_guardar.config(state="disabled")
        self.boton_modifi.config(state="disabled")
        self.boton_eliminar.config(state="disabled")

    def guardar_dat(self):
        """Función de guardar datos"""
        print(f"Guardando: {self.mi_nombre.get()}, {self.mi_cantidad.get()}, {self.mi_precio.get()}, {self.mi_descripcion.get()}")
        self.Des_campos()  # Luego de guardar, desactivar los campos

    
        





frame = MiFrame(ventana)
ventana.mainloop()
