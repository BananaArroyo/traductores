from tkinter import messagebox
from tkinter import filedialog

import os 
from os import scandir, walk

import validations as val

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

def read_file(archivo_abierto,main_nmonic):
    # if archivo_abierto == "":
    #     messagebox.showwarning(message=f"Agregue un archivo", title="Notification")
    #     return 

    archivo = open(archivo_abierto.get(), "r") 
    
    for renglon in archivo.readlines():
        cont = 0
        for palabra in renglon.split(' '):
            if val.validar_comentario(palabra) and cont<1: #comentario en primer palabra
                write_comment(renglon)
                break #rompe ciclo for si encuentr el renglon comentado
            else:
                if val.nmonico(palabra) and cont == 0:
                    cont+=1
                    write_file(cont, palabra, main_nmonic, nmon = True)
                    
                else:
                    write_file(cont, palabra, main_nmonic)
            
            cont += 1
                    
    archivo.close()
    messagebox.showinfo(message=f"Codigo compilado con EXITO", title="Notification")

def write_file(contador=0, palabra="", main_nmonic="", nmon = False):
    archivo = open("Practica 2.txt", "a")
    
    if contador == 0:   #Etiqueta
        archivo.write(f"\nETI\t{palabra}\n")
    elif contador == 1: #Nmonico
        if nmon:
            archivo.write(f"\nNM\t{palabra}\n")
        else:
            archivo.write(f"NM\t{palabra}\n")
        main_nmonic.set(palabra)
    elif contador == 2: #Operador
        md, obj1, obj2, size, obj3 = val.addressMode(main_nmonic.get(), palabra)
        archivo.write(f"OP\t{palabra}")
        archivo.write(f"MD\t{md}\n")
        archivo.write(f"CO\t{obj1} {obj2} {obj3}\n")
        archivo.write(f"SZ\t{size}\n")
    elif contador == 3: #Comentario
        archivo.write(f"COM\t{palabra}\n")
    else:   #Errores
        archivo.write(f"ERR\t{palabra}\n")

    archivo.close()

def write_comment(renglon):
    archivoC = open("Practica 2.txt", "a")
    archivoC.write(f"COM\t{renglon}\n")
    archivoC.close()