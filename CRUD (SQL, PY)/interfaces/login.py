from tkinter import *
from tkinter import messagebox
import mysql.connector

ventana = Tk()
ventana.title("Login")
ventana.geometry("673x771+611+141")
#ventana.resizable(False,False)
#ventana.overrideredirect(True)

#icon image
imgICo=PhotoImage(file="img/LOG4iIni.png")
ventana.iconphoto(False,imgICo)
#background image
frame=Frame(ventana, width=100, height=390)
frame.pack(fill=Y)
backgroundimage=PhotoImage(file="img/LOG4iIni.png")
Label(frame,image=backgroundimage).pack()

img_user = PhotoImage(file="img/user1.png")
label_user = Label(ventana, image=img_user)
label_user.place(x=100, y=390)

img_contra = PhotoImage(file="img/Contra.png")
label_contra = Label(ventana, image=img_contra)
label_contra.place(x=160, y=500)


user = Entry(frame, width=18)
user.pack()







ventana.img_user = img_user
ventana.img_contra = img_contra
ventana.backgroundimage = backgroundimage
ventana.mainloop()