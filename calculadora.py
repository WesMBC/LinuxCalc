from tkinter import *
from tkinter import ttk
import math


root = Tk()

root.title("Calculadora")
root.geometry("+350+200")


#Estilos 

estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure('mainframe.TFrame', background = "#DBDBDB")

mainframe = ttk.Frame(root,style="mainframe.TFrame")
mainframe.grid(column=0, row=0)


#estilos de label
estilo_Entrada1 = ttk.Style()
estilo_Entrada1.configure('entrada1.TLabel', font="arial 15", ANCHOR="e")

estilo_Entrada2 = ttk.Style()
estilo_Entrada2.configure('entrada1.TLabel', font="arial 40", ANCHOR="e")

entrada1 = StringVar()
label_Entrada1 = ttk.Label(mainframe,textvariable=entrada1,style="entrada1.TLabel")

entrada2 = StringVar
label_Entrada2 = ttk.Label(mainframe, textvariable=entrada2,style="entrada2.TLabel")



#estilos para botones 

estilo_Numeros = ttk.Style()
estilo_Numeros.configure('numeros.TButton',font="arial 22", width=5, Background = "#FFFFFF")

estilo_borrar = ttk.Style()
estilo_borrar.configure('borrar.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")
estilo_borrar.map("borrar.TButton", foreground=[('active', '#FFFFFF')], background=[("active","#858585")])

estilo_General_Botones = ttk.Style()
estilo_General_Botones.configure('estilo_General.TButton', font="arial 22", width=5,relief = "flat", background="#CECECE")


#Creacion de botones

boton0 = ttk.Button(mainframe, text="0", style="numeros.TButton")
boton1 = ttk.Button(mainframe, text="1", style="numeros.TButton")
boton2 = ttk.Button(mainframe, text="2", style="numeros.TButton")
boton3 = ttk.Button(mainframe, text="3", style="numeros.TButton")
boton4 = ttk.Button(mainframe, text="4", style="numeros.TButton")
boton5 = ttk.Button(mainframe, text="5", style="numeros.TButton")
boton6 = ttk.Button(mainframe, text="6", style="numeros.TButton")
boton7 = ttk.Button(mainframe, text="7", style="numeros.TButton")
boton8 = ttk.Button(mainframe, text="8", style="numeros.TButton")
boton9 = ttk.Button(mainframe, text="9", style="numeros.TButton")

botonbotonBorrar = ttk.Button(mainframe, text=chr(9003), style="borrar.TButton")
botonborrarTodo  = ttk.Button(mainframe, text="C", style="borrar.TButton")
botonparentesis1 = ttk.Button(mainframe, text="(", style="estilo_General.TButton")
botonparentesis2 = ttk.Button(mainframe, text=")", style="estilo_General.TButton")
botonpunto       = ttk.Button(mainframe, text=".", style="estilo_General.TButton") 

botonSumar       = ttk.Button(mainframe,text="+", style="estilo_General.TButton")
botonRestar      = ttk.Button(mainframe,text="-", style="estilo_General.TButton")
botonMultiplicar = ttk.Button(mainframe,text="X", style="estilo_General.TButton")
botonDividir     = ttk.Button(mainframe,text="/", style="estilo_General.TButton")

botonIgual      = ttk.Button(mainframe,text="=", style="estilo_General.TButton")
botonRaiz       = ttk.Button(mainframe,text="√", style="estilo_General.TButton")
botonPorcentaje = ttk.Button(mainframe,text="%", style="estilo_General.TButton")


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
botonMultiplicar.grid(column=3,row=5)

boton0.grid(column=0,columnspan=2,row=6,sticky=(E,W))
botonpunto.grid(column=2,row=6)
botonDividir.grid(column=3,row=6)



botonIgual.grid(column=0,columnspan=2,row=7,sticky=(E,W))
botonPorcentaje.grid(column=2,row=7)
botonRaiz.grid(column=3,row=7)


for item in mainframe.winfo_children():
    item.grid_configure(ipady=10,padx=1,pady=1)




root.mainloop()






