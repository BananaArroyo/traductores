import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

import functions

#Make main window 
ventana = ThemedTk(theme="radiance")
ventana.title("Practica 2") 

# VARS
archivo_abierto = tk.StringVar()
nmominicos = ["ABA","ABX","ABY","ADCA","ADCB","ADDA","ADDB","ADDD","ANDA","ANDB","ANDCC","ASL","ASLA","ASLB","ASLD","ASR","ASRA","ASRB","BCC","BCLR"]

#Tkinter widgets
ttk.Button(text = "Abrir Archivo", command = lambda: functions.select_file(archivo_abierto)).grid(row = 1, column = 0, ipady = 5, ipadx = 5)
ttk.Button(text = "Procesar", command = lambda: functions.read_file(archivo_abierto)).grid(row = 2, column = 0, ipady = 5, ipadx = 5)

#Run main window
ventana.mainloop()