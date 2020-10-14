import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

import functions

#Make main window 
ventana = ThemedTk(theme="radiance")
ventana.title("Practica 2") 

# Clases

class Archivo:
    pass
    # nombre = ""
    # memoria = ""

class Codigo:
    pass
    # etiqueta = ""
    # nmonico = ""
    # modo_dir = ""
    # comentario = ""

archivo = Archivo()
codigo = Codigo()


#Tkinter widgets
ttk.Button(text = "Abrir Archivo", command = lambda: functions.select_file(archivo)).grid(row = 1, column = 0, ipady = 5, ipadx = 5)

ttk.Button(text = "Procesar", command = lambda: functions.read_file(archivo, codigo)).grid(row = 2, column = 0, ipady = 5, ipadx = 5)

#Run main window
ventana.mainloop()