import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import mysql.connector  # Importar el conector de MySQL


def abrir_github():
    webbrowser.open("https://github.com/MN03SGO")


def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="root",
            database="Sistema"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

ventana = tk.Tk()
ventana.title("CRUD")




try:
    
    img_boton_nuevo = Image.open("img/Nuevo.png")
    img_boton_nuevo = ImageTk.PhotoImage(img_boton_nuevo)

    img_boton_guardar = Image.open("img/Guarda.png")
    img_boton_guardar = ImageTk.PhotoImage(img_boton_guardar)

    img_boton_modifi = Image.open("img/Modify.png")
    img_boton_modifi = ImageTk.PhotoImage(img_boton_modifi)

    img_boton_cancelar = Image.open("img/Cancelar.png")
    img_boton_cancelar = ImageTk.PhotoImage(img_boton_cancelar)

    img_boton_elimi = Image.open("img/Eliminar.png")
    img_boton_elimi = ImageTk.PhotoImage(img_boton_elimi)

except Exception as e:
    print("No se pudieron cargar las imágenes:", e)

# Barra de menú
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
    #constructor
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=0, column=0, padx=50, pady=50, sticky="nsew")
        self.columnconfigure((0, 1, 2), weight=1)
        self.campo_galleta()
        self.Des_campos()
        self.tabla_galletas()
        self.cargar_datos_tabla()
        self.campo_buscar()
        #TEXTOS Y ENTRADAS
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

        # Botones
        boton_frame = tk.Frame(self)
        boton_frame.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")
        boton_frame.columnconfigure((0, 1, 2, 3), weight=1)

        # BTN NUEVO
        self.boton_nuevo = tk.Button(boton_frame, text="Nuevo", font=("Arial", 14, "bold"),
                                    fg="black",
                                    image=img_boton_nuevo, compound="left",
                                    width=170, height=60,
                                    command=self.Hab_campos)
        self.boton_nuevo.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # BTN GUARDAR
        self.boton_guardar = tk.Button(boton_frame, text="Guardar", font=("Arial", 14, "bold"),
                                    bg="green", fg="white",
                                    image=img_boton_guardar, compound="left",
                                    width=170, height=60,
                                    command=self.guardar_dat)
        self.boton_guardar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # BTN MODIFICAR
        self.boton_modifi = tk.Button(boton_frame, text="Modificar", font=("Arial", 14, "bold"),
                                    bg="blue", fg="white",
                                    image=img_boton_modifi, compound="left",
                                    width=170, height=60,
                                    cursor="hand2",
                                    command=self.modificar_dat)
        self.boton_modifi.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # BTN CANCELAR
        self.boton_cancelar = tk.Button(boton_frame, text="Cancelar", font=("Arial", 14, "bold"),
                                        bg="red", fg="white",
                                        image=img_boton_cancelar, compound="left",
                                        width=170, height=60,
                                        command=self.Des_campos)
        self.boton_cancelar.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        # BTN ELIMINAR
        self.boton_eliminar = tk.Button(boton_frame, text="Eliminar", font=("Arial", 14, "bold"),
                                        bg="red", fg="white",
                                        image=img_boton_elimi, compound="left",
                                        width=170, height=60,
                                        command=self.eliminar_dat)
        self.boton_eliminar.grid(row=0, column=4, padx=5, pady=5, sticky="ew")

    def Hab_campos(self):
        self.entry_nombre.config(state="normal")
        self.entry_cantidad.config(state="normal")
        self.entry_precio.config(state="normal")
        self.entry_descripcion.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_modifi.config(state="normal")
        self.boton_cancelar.config(state="normal")
        self.boton_eliminar.config(state="normal")

    def Des_campos(self):
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
        self.boton_cancelar.config(state="disabled")
        self.boton_eliminar.config(state="disabled")

    def guardar_dat(self):
        
        nombre = self.mi_nombre.get()
        cantidad = self.mi_cantidad.get()
        precio = self.mi_precio.get()
        descripcion = self.mi_descripcion.get()

        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = "INSERT INTO galletas (nombre, cantidad, precio, descripcion) VALUES (%s, %s, %s, %s)"
                valores = (nombre, cantidad, precio, descripcion)
                cursor.execute(sql, valores)
                conexion.commit()
                print("Datos guardados correctamente.")
                self.cargar_datos_tabla()  
                self.Des_campos()
            except mysql.connector.Error as err:
                print(f"Error al guardar datos: {err}")
            finally:
                cursor.close()
                conexion.close()

    def modificar_dat(self):
        
        seleccion = self.tabla.selection()
        if seleccion:
            id_galleta = self.tabla.item(seleccion, "text")
            nombre = self.mi_nombre.get()
            cantidad = self.mi_cantidad.get()
            precio = self.mi_precio.get()
            descripcion = self.mi_descripcion.get()

            conexion = conectar_bd()
            if conexion:
                try:
                    cursor = conexion.cursor()
                    sql = "UPDATE galletas SET nombre = %s, cantidad = %s, precio = %s, descripcion = %s WHERE id = %s"
                    valores = (nombre, cantidad, precio, descripcion, id_galleta)
                    cursor.execute(sql, valores)
                    conexion.commit()
                    print("Datos modificados correctamente.")
                    self.cargar_datos_tabla() 
                    self.Des_campos()
                except mysql.connector.Error as err:
                    print(f"Error al modificar datos: {err}")
                finally:
                    cursor.close()
                    conexion.close()

    def eliminar_dat(self):
        
        seleccion = self.tabla.selection()
        if seleccion:
            id_galleta = self.tabla.item(seleccion, "text")

            conexion = conectar_bd()
            if conexion:
                try:
                    cursor = conexion.cursor()
                    sql = "DELETE FROM galletas WHERE id = %s"
                    valores = (id_galleta,)
                    cursor.execute(sql, valores)
                    conexion.commit()
                    print("Datos eliminados correctamente.")
                    self.cargar_datos_tabla() 
                    self.Des_campos()
                except mysql.connector.Error as err:
                    print(f"Error al eliminar datos: {err}")
                finally:
                    cursor.close()
                    conexion.close()

    def cargar_datos_tabla(self):
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id, nombre, cantidad, precio, descripcion FROM galletas")
                rows = cursor.fetchall()

                for item in self.tabla.get_children():
                    self.tabla.delete(item)

                for row in rows:
                    self.tabla.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4]))
            except mysql.connector.Error as err:
                print(f"Error al cargar datos: {err}")
            finally:
                cursor.close()
                conexion.close()
    #tabla de tk 
    def tabla_galletas(self):
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)

        frame_tabla = tk.Frame(self)
        frame_tabla.grid(row=5, column=0, columnspan=4, pady=10, sticky="nsew")
        frame_tabla.rowconfigure(0, weight=1)
        frame_tabla.columnconfigure(0, weight=1)

        self.tabla = ttk.Treeview(frame_tabla, columns=("Nombre", "Cantidad", "Precio", "Descripcion"))
        self.tabla.grid(row=0, column=0, sticky="nsew")

        # Agregar scrollbar  de tkinter
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.heading("Descripcion", text="Descripción")

        
        self.tabla.bind("<<TreeviewSelect>>", self.cargar_datos_seleccionados)

    def cargar_datos_seleccionados(self, event):
        seleccion = self.tabla.selection()
        if seleccion:
            item = self.tabla.item(seleccion)
            valores = item['values']
            if valores:
                self.mi_nombre.set(valores[0])
                self.mi_cantidad.set(valores[1])
                self.mi_precio.set(valores[2])
                self.mi_descripcion.set(valores[3])
                self.Hab_campos()


    ##BUSCAR 
    def campo_buscar(self):
        self.label_buscar = tk.Label(self, text="Buscar Galleta:", font=("Arial", 18, "bold"))
        self.label_buscar.grid(row=6, column=0, padx=10, pady=10, sticky="e")

        self.mi_busqueda = tk.StringVar()
        self.entry_buscar = tk.Entry(self, textvariable=self.mi_busqueda, font=("Arial", 18), width=35)
        self.entry_buscar.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        self.boton_buscar = tk.Button(self, text="Buscar", font=("Arial", 14, "bold"), command=self.buscar_galleta)
        self.boton_buscar.grid(row=6, column=2, padx=10, pady=10, sticky="w")

    def buscar_galleta(self):
        termino = self.mi_busqueda.get()
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id, nombre, cantidad, precio, descripcion FROM galletas WHERE nombre LIKE %s", ("%" + termino + "%",))
                rows = cursor.fetchall()

                for item in self.tabla.get_children():
                    self.tabla.delete(item)

                for row in rows:
                    self.tabla.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4]))
            except mysql.connector.Error as err:
                print(f"Error en la búsqueda: {err}")
            finally:
                cursor.close()
                conexion.close()


frame = MiFrame(ventana)
ventana.mainloop()   
#by SIGARAN