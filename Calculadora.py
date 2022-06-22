from ast import Lambda
from curses import color_content, flushinp
from email.headerregistry import HeaderRegistry
from tkinter import *
from turtle import width
from math import *

cal=Tk()

def botonClick(num):
    global operador
    operador=operador+str(num)
    entrada.set(operador)

def resultado():
    global operador
    try:
        resolver=str(eval(operador))    
        entrada.set(resolver)
    except:
        entrada.set("Error")
    operador=""

def borrar():
    global operador
    operador=("")
    entrada.set("0")

entrada =StringVar()
operador=""
#Formato de ventana
cal.title("La Calculadora de Flork")
cal.configure(background="gray")

#FOrmato de Botones
alto=2
ancho=3

#Display
color="#747f91"
color2="#747f92"
display=Entry(cal,font=("comic sans",15),bd=10,justify="right",textvariable=entrada)
display.grid(row=0, column=0,columnspan=5)

#Botones

Button(cal,text=1,bg=color,width=ancho,height=alto,command=lambda:botonClick(1)).grid(row=1, column=0 )
Button(cal,text=2,bg=color,width=ancho,height=alto,command=lambda:botonClick(2)).grid(row=1, column=1 )
Button(cal,text=3,bg=color,width=ancho,height=alto,command=lambda:botonClick(3)).grid(row=1, column=2 )

Button(cal,text=4,bg=color,width=ancho,height=alto,command=lambda:botonClick(4)).grid(row=2, column=0 )
Button(cal,text=5,bg=color,width=ancho,height=alto,command=lambda:botonClick(5)).grid(row=2, column=1 )
Button(cal,text=6,bg=color,width=ancho,height=alto,command=lambda:botonClick(6)).grid(row=2, column=2 )

Button(cal,text=7,bg=color,width=ancho,height=alto,command=lambda:botonClick(7)).grid(row=3, column=0 )
Button(cal,text=8,bg=color,width=ancho,height=alto,command=lambda:botonClick(8)).grid(row=3, column=1 )
Button(cal,text=9,bg=color,width=ancho,height=alto,command=lambda:botonClick(9)).grid(row=3, column=2 )
Button(cal,text=0,bg=color,width=ancho,height=alto,command=lambda:botonClick(0)).grid(row=4, column=1 )

Button(cal,text="AC",bg=color2,width=ancho,height=alto,command=lambda:borrar()).grid(row=1, column=3)
Button(cal,text="=",bg=color2,width=ancho,height=alto,command=lambda:resultado()).grid(row=4, column=3)
Button(cal,text=".",bg=color2,width=ancho,height=alto,command=lambda:botonClick(".")).grid(row=1, column=4)
Button(cal,text="\u00F7",bg=color2,width=ancho,height=alto,command=lambda:botonClick("/")).grid(row=2, column=3 )
Button(cal,text="*",bg=color2,width=ancho,height=alto,command=lambda:botonClick("*")).grid(row=3, column=3)
Button(cal,text="+",bg=color2,width=ancho,height=alto,command=lambda:botonClick("+")).grid(row=2, column=4)
Button(cal,text="-",bg=color2,width=ancho,height=alto,command=lambda:botonClick("-")).grid(row=3, column=4)
Button(cal,text="(",bg=color2,width=ancho,height=alto,command=lambda:botonClick("(")).grid(row=4, column=0)
Button(cal,text=")",bg=color2,width=ancho,height=alto,command=lambda:botonClick(")")).grid(row=4, column=2)

cal.mainloop()  
