from tkinter import *
from tkinter import ttk
import math

#Funciones para calulo

caracteresValidos = ["1","2","3","4","5","6","7","8","9","0","(",")",".","-","+","/","x","X","*","=","c","C"]

def parenthesis(calculacion:str):
    if not isinstance(calculacion,str):
        raise TypeError("El argumento debe ser una cadena de texto que contenga un calculo matematico")
    
    calculacion = calculacion.replace("((","(")
    calculacion = calculacion.replace("))",")")
    calculacion = calculacion.replace("(","i")
    calculacion = calculacion.replace(")","i")
    
    elementos = calculacion.split("i")
    resultado = 1

    for contenido in elementos:
        if contenido == "":
            continue
        resultado = resultado*eval(contenido)

    return resultado



def ingresarValores(tecla):
    if tecla in caracteresValidos:
        entrada2.set(entrada2.get() + tecla)
        
def borrarTodo(tecla):
    if tecla == "c" or tecla == "C":
        entrada2.set("")

def borrarUno(tecla):
    if tecla == chr(9003):
        nuevaEntrada = entrada2.get()
        entrada2.set(nuevaEntrada[0:-1])

def calulcar(tecla):

    calculo = entrada2.get()
    resultado = 0
    if tecla == "=":
        if "(" in calculo or ")" in calculo:
            resultado = parenthesis(calculo)
            print(resultado)
            entrada1.set(str(resultado))
            return True
        entrada1.set(eval(entrada2.get()))
        return True
    else:
        return False


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

entrada2 = StringVar()
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

boton0 = ttk.Button(mainframe, text="0", style="numeros.TButton", command=lambda:ingresarValores("0"))
boton1 = ttk.Button(mainframe, text="1", style="numeros.TButton", command=lambda:ingresarValores("1"))
boton2 = ttk.Button(mainframe, text="2", style="numeros.TButton", command=lambda:ingresarValores("2"))
boton3 = ttk.Button(mainframe, text="3", style="numeros.TButton", command=lambda:ingresarValores("3"))
boton4 = ttk.Button(mainframe, text="4", style="numeros.TButton", command=lambda:ingresarValores("4"))
boton5 = ttk.Button(mainframe, text="5", style="numeros.TButton", command=lambda:ingresarValores("5"))
boton6 = ttk.Button(mainframe, text="6", style="numeros.TButton", command=lambda:ingresarValores("6"))
boton7 = ttk.Button(mainframe, text="7", style="numeros.TButton", command=lambda:ingresarValores("7"))
boton8 = ttk.Button(mainframe, text="8", style="numeros.TButton", command=lambda:ingresarValores("8"))
boton9 = ttk.Button(mainframe, text="9", style="numeros.TButton", command=lambda:ingresarValores("9"))

botonbotonBorrar = ttk.Button(mainframe, text=chr(9003), style="borrar.TButton", command=lambda:borrarUno(chr(9003)))
botonborrarTodo  = ttk.Button(mainframe, text="C", style="borrar.TButton", command=lambda:borrarTodo("C"))
botonparentesis1 = ttk.Button(mainframe, text="(", style="estilo_General.TButton", command=lambda:ingresarValores("("))
botonparentesis2 = ttk.Button(mainframe, text=")", style="estilo_General.TButton", command=lambda:ingresarValores(")"))
botonpunto       = ttk.Button(mainframe, text=".", style="estilo_General.TButton", command=lambda:ingresarValores(".")) 

botonSumar       = ttk.Button(mainframe,text="+", style="estilo_General.TButton", command=lambda:ingresarValores("+"))
botonRestar      = ttk.Button(mainframe,text="-", style="estilo_General.TButton", command=lambda:ingresarValores("-"))
botonMultiplicar = ttk.Button(mainframe,text="*", style="estilo_General.TButton", command=lambda:ingresarValores("*"))
botonDividir     = ttk.Button(mainframe,text="/", style="estilo_General.TButton", command=lambda:ingresarValores("/"))

botonIgual      = ttk.Button(mainframe,text="=", style="estilo_General.TButton", command=lambda:calulcar("="))
botonRaiz       = ttk.Button(mainframe,text="√", style="estilo_General.TButton", command=lambda:ingresarValores("√"))
botonPorcentaje = ttk.Button(mainframe,text="%", style="estilo_General.TButton", command=lambda:ingresarValores("%"))


#Ubicacion en pantalla

label_Entrada1.grid(column=0,row=0, columnspan=4, sticky=(W,E))
label_Entrada2.grid(column=0,row=1, columnspan=4, sticky=(W,E))

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






