from tkinter import *
import mysql.connector

###ARREGLO DE VENTANA

ventana= Tk()
ventana.title("CRUD")
ventana.geometry("1920x1980")





imagenUsu = PhotoImage(file = "img/USUARIO1.png").grid(sticky=W)
label_imgUsu = Label(ventana, image=imagenUsu)
label_imgUsu.place(x=1202, y=340)

ventana.imagenUsu = imagenUsu

mainloop()