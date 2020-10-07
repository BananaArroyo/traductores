from tkinter import messagebox
from tkinter import filedialog

import os 
from os import scandir, walk

import validations as val

def select_file(archivo_abierto, bol_open):
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
        bol_open.set(1)

def read_file(archivo_abierto,main_nmonic):
    if archivo_abierto == "":
        messagebox.showwarning(message=f"Agregue un archivo", title="Notification")
        return

    archivo = open(archivo_abierto.get(), "r") 
    
    for renglon in archivo.readlines():
        cont = 0
        for palabra in renglon.split(' '):
            escribir_archivo(cont, palabra, main_nmonic)
            cont += 1
                    
    archivo.close()
    messagebox.showinfo(message=f"Codigo compilado con EXITO", title="Notification")

def escribir_archivo(contador=0, palabra="", main_nmonic=""):
    archivo = open("Practica 1.txt", "a")
    
    if contador == 0:   #Etiqueta
        archivo.write(f"ETI\t{palabra}\n")
    elif contador == 1: #Nmonico
        archivo.write(f"NM\t{palabra}\n")
        main_nmonic.set(palabra)
    elif contador == 2: #Operador
        archivo.write(f"OP\t{palabra}\n")
        
        md, obj1, obj2, size = val.addressMode(main_nmonic.get(), palabra)

        archivo.write(f"MD\t{md}\n")
        archivo.write(f"CO\t{obj1} {obj2}\n")
        archivo.write(f"SZ\t{size}\n")

    elif contador == 3: #Comentario
        archivo.write(f"COM\t{palabra}\n")
    else:   #Errores
        archivo.write(f"ERR\t{palabra}\n")

    archivo.close()