from tkinter import *
from tkinter import ttk
import math

#Funciones para calulo

caracteresValidos = ["1","2","3","4","5","6","7","8","9","0","(",")",".","-","+","/","x","X","*","=","c","C"]

def keyboardInput(event):
    #print("you have pressed: " + event.keysym)
    if event.keysym in ["Return","KP_Enter"]:
        calcular("=")
        return True
    if event.keysym in ["BackSpace"]:
        borrarUno(chr(9003))
        return True
    if event.keysym in ["Delete"]:
        borrarTodo("c")
        return True

    entrada2.set(entrada2.get()+event.char)
    return True


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



def parenthesis(calculacion:str):
    if not isinstance(calculacion,str):
        raise TypeError("El argumento debe ser una cadena de texto que contenga un calculo matematico")
    
    calculacion = calculacion.replace("(","i")
    calculacion = calculacion.replace(")","i")
    
    elementos = calculacion.split("i")
    print(elementos)
    resultado = 1

    for elemento in elementos:
        if elemento == "":
            continue
        print(elemento)
        resultado = resultado*calculo(elemento)
    
    return resultado
    

def division (calculacion:str):
    """
    Funcion que recibe una cadena de caracteres que son numero con una division del simbolo /
    retornando: el numerados evaluado y el denominados evaluados

    """
    if not isinstance(calculacion,str):
        raise TypeError("El argumento debe ser una cadena de texto que contenga un calculo matematico")
    
    if "/" not in calculacion:
        raise TypeError("Tiene que tener un simbolo de division para poder usar esta funcion ")
    elif "/" in calculacion:
        calculaciones = calculacion.split("/")
        respuestas = []
        resultado = 1
        for problema in calculaciones:
            respuestas.append(calculo(problema))
        for i in range(len(respuestas)-1,0,-1):
            resultado = respuestas[i]/resultado
            print(f"el resultado es {resultado}")
        return  resultado
    return False
        

def calculo(problema:str):
    """
    Funcion para la administracion de las ejecuciones de calculos matematicos de la caluladora
    """
    if not isinstance(problema,str):
        raise TypeError("El argumento debe ser una cadena de texto que contenga un calculo matematico")
    else:
        resultado = 0
        if "/" in problema:
            resultado = division(problema)
        elif "(" in problema:
            resultado = parenthesis(problema)
        else:
            print(f"el problema es {problema}")
            resultado = eval(problema)
        
        return resultado
    

def calcular(tecla):

    if tecla != "=":
        raise TypeError("no es el caracter =") 
    elif tecla == "=":
        if entrada2.get() == "":
            entrada1.set("vacio")
            return True
        entrada1.set(calculo(entrada2.get()))
        return True
    else:
        return False


root = Tk()
root.bind("<Key>", keyboardInput)


root.title("Calculadora")
root.geometry("+350+200")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

#Estilos 

estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure('mainframe.TFrame', background = "#DBDBDB")

mainframe = ttk.Frame(root,style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W,N,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.columnconfigure(1,weight=1)
mainframe.columnconfigure(2,weight=1)
mainframe.columnconfigure(3,weight=1)

mainframe.rowconfigure(0,weight=1)
mainframe.rowconfigure(1,weight=1)
mainframe.rowconfigure(2,weight=1)
mainframe.rowconfigure(3,weight=1)
mainframe.rowconfigure(4,weight=1)
mainframe.rowconfigure(5,weight=1)
mainframe.rowconfigure(6,weight=1)
mainframe.rowconfigure(7,weight=1)


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
estilo_General_Botones.map('estilo_General.TButton', foreground=[('active', '#FF3300')], background = [("active","#FFFFFF")])

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

botonIgual      = ttk.Button(mainframe,text="=", style="estilo_General.TButton", command=lambda:calcular("="))
botonRaiz       = ttk.Button(mainframe,text="√", style="estilo_General.TButton", command=lambda:ingresarValores("√"))
botonPorcentaje = ttk.Button(mainframe,text="%", style="estilo_General.TButton", command=lambda:ingresarValores("%"))


#Ubicacion en pantalla

label_Entrada1.grid(column=0,row=0, columnspan=4)
label_Entrada2.grid(column=0,row=1, columnspan=4)

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

boton0.grid(column=0,columnspan=2,row=6)
botonpunto.grid(column=2,row=6)
botonDividir.grid(column=3,row=6)



botonIgual.grid(column=0,columnspan=2,row=7)
botonPorcentaje.grid(column=2,row=7)
botonRaiz.grid(column=3,row=7)


for item in mainframe.winfo_children():
    item.grid_configure(ipady=10,padx=1,pady=1)

for item in mainframe.winfo_children():
    item.grid_configure(sticky=(W,N,E,S))


root.mainloop()






