from tkinter import *
from tkinter import ttk
import math


root = Tk()

root.title("Calculadora")
root.geometry("+350+200")


#Estilos 
"""
estilos = ttk.Style()
estilos.configure('mainframe.Tframe', background = "#DBDBDB")
"""

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)


entrada1 = StringVar()
label_Entrada1 = ttk.Label(mainframe,textvariable=entrada1)

entrada2 = StringVar
label_Entrada2 = ttk.Label(mainframe, textvariable=entrada2)




#Creacion de botones

boton0 = ttk.Button(mainframe, text="0")
boton1 = ttk.Button(mainframe, text="1")
boton2 = ttk.Button(mainframe, text="2")
boton3 = ttk.Button(mainframe, text="3")
boton4 = ttk.Button(mainframe, text="4")
boton5 = ttk.Button(mainframe, text="5")
boton6 = ttk.Button(mainframe, text="6")
boton7 = ttk.Button(mainframe, text="7")
boton8 = ttk.Button(mainframe, text="8")
boton9 = ttk.Button(mainframe, text="9")

botonbotonBorrar = ttk.Button(mainframe, text=chr(9003))
botonborrarTodo  = ttk.Button(mainframe, text="C")
botonparentesis1 = ttk.Button(mainframe, text="(")
botonparentesis2 = ttk.Button(mainframe, text=")")
botonpunto       = ttk.Button(mainframe, text=".") 

botonSumar       = ttk.Button(mainframe,text="+")
botonRestar      = ttk.Button(mainframe,text="-")
botonMultiplicar = ttk.Button(mainframe,text="X")
botonDividir     = ttk.Button(mainframe,text="/")

botonIgual = ttk.Button(mainframe,text="=")
botonRaiz  = ttk.Button(mainframe,text="√")


#Ubicacion en pantalla

label_Entrada1.grid(column=0,row=0)
label_Entrada2.grid(column=0,row=1)

botonparentesis1.grid(column=0,row=2)
botonparentesis2.grid(column=1,row=2)
botonborrarTodo.grid(column=2,row=2)
botonbotonBorrar.grid(column=3,row=2)

boton9.grid(column=0,row=3)
boton8.grid(column=1,row=3)
boton7.grid(column=2,row=3)
botonSumar.grid(column=3,row=3)

boton6.grid(column=0,row=4)
boton5.grid(column=1,row=4)
boton4.grid(column=2,row=4)
botonRestar.grid(column=3,row=4)

boton3.grid(column=0,row=5)
boton2.grid(column=1,row=5)
boton1.grid(column=2,row=5)
botonMultiplicar.grid(column=3,row=5,sticky=(E,W))

boton0.grid(column=0,row=6)
botonpunto.grid(column=1,row=6)
botonIgual.grid(column=2,row=6)
botonDividir.grid(column=3,row=6)







root.mainloop()






