from tkinter import *

ventana = Tk()
ventana.title("Login")
ventana.geometry("673x771+611+141")

# Icono de la ventana
imgICo = PhotoImage(file="img/LOG4iIni.png")
ventana.iconphoto(False, imgICo)

# Imagen de fondo
frame = Frame(ventana, width=100, height=390)
frame.pack(fill=Y)
backgroundimage = PhotoImage(file="img/LOG4iIni.png")
Label(frame, image=backgroundimage).pack()
ventana.overrideredirect(True)

# Ícono y campo de usuario
img_user = PhotoImage(file="img/user1.png")
label_user = Label(ventana, image=img_user)
label_user.place(x=200, y=390)

user = Entry(ventana, width=18, font=("Arial", 14))
user.place(x=250, y=400)  # Ajusta la posición para estar al lado del icono

# Ícono y campo de contraseña
img_contra = PhotoImage(file="img/Contra.png")
label_contra = Label(ventana, image=img_contra)
label_contra.place(x=200, y=460)

contra = Entry(ventana, width=18, font=("Arial", 14), show="*")
contra.place(x=250, y=470)  # Ajusta la posición

# Botón de inicio de sesión
btn_login = Button(ventana, text="Iniciar Sesión", font=("Arial", 14))
btn_login.place(x=270, y=520)

# Mantener referencia a las imágenes
ventana.img_user = img_user
ventana.img_contra = img_contra
ventana.backgroundimage = backgroundimage

ventana.mainloop()
