from tkinter import *
from tkinter import messagebox
import mysql.connector


def verificar_login():
    usuario = user.get()
    password = contra.get()
    try: 
        conexion = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="root", 
            database="Sistema"
        )
        cursor = conexion.cursor()
        consulta = "SELECT * FROM login WHERE NombreUsu = %s AND Contra = %s"
        cursor.execute(consulta, (usuario, password))
        resultado = cursor.fetchone()
        if resultado:
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo conectar a la BD: {err}")

ventana = Tk()
ventana.title("Login")
ventana.geometry("673x771+611+141")

imgICo = PhotoImage(file="img/LOG4iIni.png")
ventana.iconphoto(False, imgICo)

frame = Frame(ventana, width=100, height=390)
frame.pack(fill=Y)
backgroundimage = PhotoImage(file="img/LOG4iIni.png")
Label(frame, image=backgroundimage).pack()
# usu
img_user = PhotoImage(file="img/user1.png")
label_user = Label(ventana, image=img_user)
label_user.place(x=200, y=390)
user = Entry(ventana, width=18, font=("Arial", 14))
user.place(x=250, y=400)

# contra
img_contra = PhotoImage(file="img/Contra.png")
label_contra = Label(ventana, image=img_contra)
label_contra.place(x=200, y=460)
contra = Entry(ventana, width=18, font=("Arial", 14), show="*")
contra.place(x=250, y=470)


btn_login = Button(ventana, text="Iniciar Sesión", font=("Arial", 14), command=verificar_login)
btn_login.place(x=270, y=520)

ventana.img_user = img_user
ventana.img_contra = img_contra
ventana.backgroundimage = backgroundimage
ventana.mainloop()
#by Sigaran