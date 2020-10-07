import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

import functions

#Make main window 
ventana = ThemedTk(theme="radiance")
ventana.title("Practica 2") 

# VARS
archivo_abierto = tk.StringVar()#Archivo que se procesara (*.asm)
main_nmonic = tk.StringVar()    #Nmonico con el que se trabaja

#Tkinter widgets
ttk.Button(text = "Abrir Archivo", command = lambda: functions.select_file(archivo_abierto)).grid(row = 1, column = 0, ipady = 5, ipadx = 5)

ttk.Button(text = "Procesar", command = lambda: functions.read_file(archivo_abierto, main_nmonic)).grid(row = 2, column = 0, ipady = 5, ipadx = 5)

#Run main window
ventana.mainloop()