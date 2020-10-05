from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import os 
from os import scandir, walk

import functions

ventana = Tk()
ventana.title("Practica 2") 

def seleccionar_archivo():
    global archivo_abierto
    archivo_abierto = filedialog.askopenfilename(
                    title = "Selecciona un archivo", 
                    filetypes = (("asm files", "*.asm"), ("txt files", "*.txt"), ("all files", "*.*"))
                    ) #initialdir = "/", (Agregarlo para abrir en directorio raiz)

    if archivo_abierto == "":
        messagebox.showwarning(message="No se cargo ningun archivo", title="Notification")
    else:   
        archivo_abierto = os.path.basename(archivo_abierto)
        messagebox.showinfo(message=f"Archivo {archivo_abierto} fue guardado", title="Notification")

def leer_archivo():
    global archivo_abierto
    print (archivo_abierto)
    archivo = open(archivo_abierto, "r") 
    
    for renglon in archivo.readlines():
        cont = 0
        for palabra in renglon.split(' '):
            cont += 1
            functions.escribir_archivo(cont, palabra)
                    
    archivo.close()
    messagebox.showinfo(message=f"Codigo compilado con exito", title="Notification")

archivo_abierto = ""

#Tkinter widgets
Button(text = "Abrir Archivo", command = seleccionar_archivo).place(x=10, y=10)
Button(text = "Procesar", command = leer_archivo).place(x=10, y=40)

ventana.mainloop()