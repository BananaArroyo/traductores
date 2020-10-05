from tkinter import messagebox
from tkinter import filedialog

import os 
from os import scandir, walk

def select_file(archivo_abierto):
    archivo = filedialog.askopenfilename(
                    title = "Selecciona un archivo", 
                    filetypes = (("asm files", "*.asm"), ("txt files", "*.txt"), ("all files", "*.*"))
                    ) #initialdir = "/", (Agregarlo para abrir en directorio raiz)
    archivo_abierto.set(archivo)
    if archivo_abierto.get() == "":
        messagebox.showwarning(message="No se cargo ningun archivo", title="Notification")
    else:   
        archivo_abierto.set(os.path.basename(archivo_abierto.get()))
        messagebox.showinfo(message=f"Archivo {archivo_abierto.get()} fue guardado", title="Notification")

def read_file(archivo_abierto):
    archivo = open(archivo_abierto.get(), "r") 
    
    for renglon in archivo.readlines():
        cont = 0
        for palabra in renglon.split(' '):
            escribir_archivo(cont, palabra)
            cont += 1
                    
    archivo.close()
    messagebox.showinfo(message=f"Codigo compilado con exito", title="Notification")

def escribir_archivo(contador=0, palabra=""):
    archivo = open("Practica 2.txt", "a")
    
    if contador == 0:   #Etiqueta
        archivo.write(f"ETI\t{palabra}\n")
    elif contador == 1: #Nmonico
        archivo.write(f"NM\t{palabra}\n")
    elif contador == 2: #Operador
        archivo.write(f"OP\t{palabra}\n")
    elif contador == 3: #Comentario
        archivo.write(f"COM\t{palabra}\n")
    else:   #Errores
        archivo.write(f"ERR\t{palabra}\n")

    archivo.close()