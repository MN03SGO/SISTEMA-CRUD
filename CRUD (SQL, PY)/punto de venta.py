import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

class PuntoDeVenta:
    def __init__(self, master):
        self.master = master
        self.carrito = []
        self.total = 0.0
        
        self.crear_widgets()
        self.cargar_productos()

    def crear_widgets(self):
        # Frame para la búsqueda
        self.frame_busqueda = tk.Frame(self.master)
        self.frame_busqueda.pack(pady=10)

        self.entry_busqueda = tk.Entry(self.frame_busqueda, width=30)
        self.entry_busqueda.grid(row=0, column=0, padx=5)

        self.boton_buscar = tk.Button(self.frame_busqueda, text="Buscar", command=self.buscar_producto)
        self.boton_buscar.grid(row=0, column=1, padx=5)

        # Frame para la lista de productos
        self.frame_productos = tk.Frame(self.master)
        self.frame_productos.pack(pady=20)

        self.label_productos = tk.Label(self.frame_productos, text="Productos", font=("Arial", 18, "bold"))
        self.label_productos.grid(row=0, column=0, padx=10, pady=10)

        self.tabla_productos = ttk.Treeview(self.frame_productos, columns=("Nombre", "Cantidad", "Precio"), show="headings")
        self.tabla_productos.grid(row=1, column=0, padx=10, pady=10)

        self.tabla_productos.heading("Nombre", text="Nombre")
        self.tabla_productos.heading("Cantidad", text="Cantidad")
        self.tabla_productos.heading("Precio", text="Precio")
        self.tabla_productos.bind("<<TreeviewSelect>>", self.agregar_al_carrito)

        # Frame para el carrito de compras
        self.frame_carrito = tk.Frame(self.master)
        self.frame_carrito.pack(pady=20)

        self.label_carrito = tk.Label(self.frame_carrito, text="Carrito de Compras", font=("Arial", 18, "bold"))
        self.label_carrito.grid(row=0, column=0, padx=10, pady=10)

        self.tabla_carrito = ttk.Treeview(self.frame_carrito, columns=("Nombre", "Precio", "Cantidad", "Subtotal"), show="headings")
        self.tabla_carrito.grid(row=1, column=0, padx=10, pady=10)

        self.tabla_carrito.heading("Nombre", text="Nombre")
        self.tabla_carrito.heading("Precio", text="Precio")
        self.tabla_carrito.heading("Cantidad", text="Cantidad")
        self.tabla_carrito.heading("Subtotal", text="Subtotal")

        # Botón para finalizar la compra
        self.boton_finalizar = tk.Button(self.master, text="Finalizar Compra", font=("Arial", 14, "bold"), bg="green", fg="white", command=self.finalizar_compra)
        self.boton_finalizar.pack(pady=10)

        self.label_total = tk.Label(self.master, text="Total: $0.00", font=("Arial", 14, "bold"))
        self.label_total.pack()

    def cargar_productos(self, filtro=""):
        self.tabla_productos.delete(*self.tabla_productos.get_children())
        try:
            conexion = mysql.connector.connect(host="localhost", user="admin", password="root", database="Sistema")
            cursor = conexion.cursor()
            consulta = "SELECT id, nombre, precio FROM galletas"
            if filtro:
                consulta += " WHERE nombre LIKE %s"
                cursor.execute(consulta, ("%" + filtro + "%",))
            else:
                cursor.execute(consulta)
            productos = cursor.fetchall()

            for producto in productos:
                self.tabla_productos.insert("", "end", values=(producto[1], 1, f"${producto[2]:.2f}"))

            conexion.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al cargar productos: {err}")

    def buscar_producto(self):
        filtro = self.entry_busqueda.get()
        self.cargar_productos(filtro)

    def agregar_al_carrito(self, event):
        seleccionado = self.tabla_productos.selection()
        if seleccionado:
            producto = self.tabla_productos.item(seleccionado, "values")
            nombre = producto[0]
            precio = float(producto[2][1:])
            cantidad = 1
            subtotal = precio * cantidad

            # Agregar al carrito
            self.carrito.append({"nombre": nombre, "precio": precio, "cantidad": cantidad, "subtotal": subtotal})

            # Mostrar en la tabla del carrito
            self.tabla_carrito.insert("", "end", values=(nombre, f"${precio:.2f}", cantidad, f"${subtotal:.2f}"))

            # Actualizar total
            self.actualizar_total()

    def actualizar_total(self):
        self.total = sum(item["subtotal"] for item in self.carrito)
        self.label_total.config(text=f"Total: ${self.total:.2f}")

    def finalizar_compra(self):
        if not self.carrito:
            messagebox.showwarning("Advertencia", "El carrito está vacío.")
            return

        messagebox.showinfo("Compra Finalizada", f"Total a pagar: ${self.total:.2f}")
        self.carrito.clear()
        self.tabla_carrito.delete(*self.tabla_carrito.get_children())
        self.actualizar_total()

ventana = tk.Tk()
ventana.title("Punto de Venta")

punto_venta = PuntoDeVenta(ventana)
ventana.mainloop()