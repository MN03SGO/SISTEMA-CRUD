from tkinter import *
import tkinter  as tk 
import mysql.connector

###ARREGLO DE VENTANA

ventana= Tk()
ventana.title("CRUD")
ventana.geometry("1920x1980")

def barra_menu(ventana):
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu, width= 300, heigth=300)

    barra_menu = tk.Menu(barra_menu)
    barra_menu.add_cascade(Label= "Inicio", menu=barra_menu)

    barra_menu.add_command(Label= "Crear registro en BD")
    barra_menu.add_command(Label= "Eliminar registro en BD")
    barra_menu.add_command(Label= "Salir")





#imagenUsu = PhotoImage(file = "img/USUARIO1.png").grid(sticky=W)
#label_imgUsu = Label(ventana, image=imagenUsu)
#label_imgUsu.place(x=1202, y=340)

#ventana.imagenUsu = imagenUsu

mainloop()