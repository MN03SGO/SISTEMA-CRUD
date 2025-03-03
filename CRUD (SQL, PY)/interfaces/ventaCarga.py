from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar #LIBRERIA DE BARRA DE CARGA
from screeninfo import get_monitors #LIBRERIA DE GESTION DE VENTANA
import os


raiz = Tk()
image = PhotoImage(file="img/MANULOGO.png")
height = 430
width = 530

monitor = get_monitors()[0] 
screen_width = monitor.width
screen_height = monitor.height
x = (screen_width // 2) - (width // 2) + monitor.x
y = (screen_height // 2) - (height // 2) + monitor.y
raiz.geometry(f"{width}x{height}+{x}+{y}")
raiz.overrideredirect(True)



raiz.image = PhotoImage(file="img/MANULOGO.png")
label = Label(raiz, image=raiz.image)
label.place(relx=0.5, rely=0.5, anchor=CENTER)

barra_progre = Label(raiz, text = "Cargando...", font=("Trebuchet M", 13, "bold"), fg="#000000")
barra_progre.place(x=200, y=390)

##AJUSTE DE LA BARRA DE CARGA
barra_estilo = ttk.Style()
barra_estilo.theme_use('clam')
barra_estilo.configure("red.Horizontal.TProgressbar", background="#007cff")
barra = Progressbar(raiz, orient=HORIZONTAL, length=400, mode='determinate', style='red.Horizontal.TProgressbar')
barra.place(x=40, y=370) 
def top():
    raiz.withdraw()
    os.system("python interfaces/login.py")
    raiz.destroy()
i = 0
def load():
    global i 
    if i <= 10:
        txt= 'Cargando...'+ (str(10*i)+'%')
        barra_progre.config(text=txt)
        barra_progre.after(600, load)
        barra['value'] = 10*i
        i +=1
    else:
        top()
#imagen del run 
imgICo=PhotoImage(file="img/LOG4iIni.png")
raiz.iconphoto(False,imgICo)
load()
raiz.resizable(False,False)
raiz.mainloop()
##by MN03SGO
