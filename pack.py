import tkinter as tk
from tkinter import ttk

#Me creo la instancia
wroot=tkinter.Tk()
#Para cambiar el título
wroot.title("Mi primera app")
#Para cambiar el tamaño de la ventana. Se informa como una cadena de texto.
wroot.geometry("800x600")
#Para cambiar la posición de la ventana en el ordenador 
wroot.geometry("800x600+0+200")
#Para calcular la anchura de mi ventana
wroot.winfo_width()
#Para calcula la altura de mi ventana
wroot.winfo_height()
#Para calcular la anchura de la pantalla
wroot.winfo_screenwidth()
#Para calcular al altura de la pantalla
wroot.winfo_screenheight()
#Para calcular la ubicación de la ventana
wroot.geometry("800x600+560+300")
#Vamos a crear un frame. Como una sección dentro de la ventana.( página 48 del manual)
fr_buttons=tkinter.Frame(wroot,width=200,height=260,bg="yellow")
fr_buttons.place(x=0,y=0)
#Vamos a crear un botón
btn_reset=tkinter.Button(fr_buttons,text="Reset")
#Lo ubicamos
btn_reset.pack(side= tkinter.TOP)
#Las opciones del frame han dejado de tener efecto al tocar las opciones del hijo. Lo arreglamos
fr_buttons.pack_propagate(False)
fr_buttons.config(width=200,height=260)

#Empezamos a configurar los botones
btn_reset.pack(fill=tkinter.X)
btn_reset.pack(fill=tkinter.Y)
btn_reset.pack(fill=tkinter.NONE)
btn_reset.pack(expand=True)
btn_reset.pack(fill=tkinter.BOTH)
btn_reset.pack(expand=False)

btn_max=tkinter.Button(fr_buttons,text="Full screen")
btn_max.pack(side=tkinter.TOP,fill=tkinter.X)

btn_centrar=tkinter.Button(fr_buttons,text="Centrar")
btn_centrar.pack(side=tkinter.BOTTOM,fill=tkinter.X)
btn_centrar.pack(side=tkinter.TOP)

btn_reset.pack(expand=True)
btn_max.pack(expand=True,fill=tkinter.BOTH)
btn_centrar.pack(expand=True,fill=tkinter.BOTH)

#Asociamos eventos a los botones
wroot.geometry()
wroot.winfo_x()
#Guardamos en una tupla, el tamaño de la ventana del eje x, del eje y, y la posición en el eje x e y de la pantalla del ordenador.
woriginals=(wroot.winfo_width(),wroot.winfo_height(),wroot.winfo_x(),wroot.winfo_y())

def reset():
    g="{}x{}+{}+{}".format(woriginals[0],woriginals[1],woriginals[2],woriginals[3])
    wroot.geometry(g)

#reset()

#Asociamos la función creada al comando. La asociación de eventos está en la página 159.

btn_reset.config(command=reset)

#Creamos los dos botones

fr_data=tkinter.Frame(wroot,width=200,height=260)
fr_data.place(x=200,y=0)
fr_data.pack_propagate(0)

fr_X=tkinter.Frame(fr_data,width=200,height=30)
lbl_name_X=tkinter.Label(fr_X, text="X:",width=5,anchor=tkinter.W)
lbl_value_X=tkinter.Label(fr_X,text="_",width=8,anchor=tkinter.W)
lbl_name_X.pack(side=tkinter.LEFT)
lbl_value_X.pack(side=tkinter.LEFT,fill=tkinter.X)
fr_X.pack(side=tkinter.TOP,fill=tkinter.X)

fr_W=tkinter.Frame(fr_data,width=200,height=30)
lbl_name_W=tkinter.Label(fr_W, text="W:",width=5,anchor=tkinter.W)
lbl_value_W=tkinter.Label(fr_W,text="_",width=8,anchor=tkinter.W)
lbl_name_W.pack(side=tkinter.LEFT)
lbl_value_W.pack(side=tkinter.LEFT,fill=tkinter.X)
fr_W.pack(side=tkinter.TOP,fill=tkinter.X)

lbl_name_X.config(anchor=tkinter.E)
lbl_name_W.config(anchor=tkinter.E)
lbl_value_W.config(anchor=tkinter.E)
lbl_value_X.config(anchor=tkinter.E)

#Evento configure página 159

def changesize(ev):
    x=wroot.winfo_x()
    w=wroot.winfo_width()
    lbl_value_X.config(text=str(x))
    lbl_value_W.config(text=str(w))

wroot.bind('<Configure>', changesize)

#Hasta ahora hemos utilizado controles con la librería de tk pero ahora vamos a utilizar la librería ttk (theme tk). 
#Utilizar ttk te permite una mayor versatilidad y te permite la misma visibilidad en windows, linux y mac.

#tk

import tkinter as tk
from tkinter import ttk

w=tk.Tk()
w.title("Comparison")

frc=tk.Frame(w)
w.pack_propagate(0)
frc.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
frc.config(bg="gray")

buc=tk.Button(frc,text="Clasico",fg="red")
frc.pack_propagate(0)
buc.pack(side=tk.TOP,fill=tk.X)
buc.config(font="Courier 34")

#ttk

frt=ttk.Frame(w)
frt.pack(side=tk.TOP,fill=tk.BOTH,expand=True)


but=ttk.Button(frt,text="themed")
frt.pack_propagate(0)
but.pack(side=tk.TOP,fill=tk.X)

s=ttk.style()
s.theme.names()
s.theme.use()

but.winfo_class()

#Para configurar el estilo, primero le ponemos un nombre miestilo, y luego la clase.

but.config(style="miestilo.TButton")
but('style')
but1=ttk.Button(frt)
but1.config(text="Otro button")
but1.pack(side=tk.TOP,fill=tk.X)
s.configure('Tbutton',font='courier 42')
s.configure('miestilo.Tbutton',background='green')










