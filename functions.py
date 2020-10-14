from tkinter import messagebox
from tkinter import filedialog

import os 
from os import scandir, walk

import validations as val

def select_file(archivo):
    #Cuando se carga inicializar la clase (Buscar: Ver los atributos de mi clase, para eliminar los existentes)
    archivo.nombre = filedialog.askopenfilename(
                    title = "Selecciona un archivo", 
                    filetypes = (("asm files", "*.asm"), ("txt files", "*.txt"), ("all files", "*.*"))
                    ) #initialdir = "/", (Agregarlo para abrir en directorio raiz)
    
    if archivo.nombre == "":
        messagebox.showwarning(message="No se cargo ningun archivo", title="Notification")
    else:   
        archivo.nombre = os.path.basename(archivo.nombre)
        messagebox.showinfo(message=f"Archivo {archivo.nombre} fue guardado", title="Notification")

def read_file(archivo, codigo):
    if not hasattr(archivo, "nombre"):
         messagebox.showwarning(message=f"Agregue un archivo", title="Notification")
    else:
        archivo.memoria = "0000"

        file = open(archivo.nombre, "r")    #Abre el archivo VAR para leerlo ("r" - Leer archivo)
        code = file.readlines() #Obtiene las lineas del archivo = [line1,line2,...,lineX]
        file.close()    #Cierra elarchivo
        #print(code)    #Imprime la lista "code" (Validación)                               
        for renglon in code:    #Itera las lineas de texto que existen en "code"
            renglon = renglon.rstrip('\n')  #elimina saltos de linea del "renglon" que se lee

            if hasattr(codigo, "etiqueta"):
                delattr(codigo,"etiqueta")
            if hasattr(codigo, "nmonico"):
                delattr(codigo,"nmonico")
            if hasattr(codigo, "operador"):
                delattr(codigo,"operador")
            if hasattr(codigo, "comentario"):
                delattr(codigo,"comentario")

            if hasattr(codigo, "addr_mode"):
                delattr(codigo,"addr_mode")
            if hasattr(codigo, "addr_value"):
                delattr(codigo,"addr_value")
            if hasattr(codigo, "memoria"):
                delattr(codigo,"memoria")
            if hasattr(codigo, "memory"):
                delattr(codigo,"memory")
            if hasattr(codigo, "obj1"):
                delattr(codigo,"obj1")
            if hasattr(codigo, "obj2"):
                delattr(codigo,"obj2")
            if hasattr(codigo, "tabsim"):
                delattr(codigo,"tabsim")

            if renglon[0] == ";":   #Si el renglon comienza con ";" (Es comentario)
                write_comment(renglon)  #Se guarda el renglon como comentario
            else:  #Si no comienza con un ";" (NO es comentario)
                cont = 0    #Cuenta el tipo de palabra 
                for palabra in renglon.split(' '):  #Itera las paabras que existen en "renglon" (Cuenta apartir de los espacios " ")
                    if cont == 0: #0 = etiqueta
                        if val.isNmonico(palabra):  #Si es una palabra reservada (NMONICO) lo guarda en nmonico (Este caso quiere decir que no existe una etiqueta)
                            codigo.nmonico = palabra    #se guarda en la clase 
                            cont+=1 #Aumenta el contador porque ta se guarda un nmonico
                        else:   #Si no es palabra reservada es una ETIQUETA
                            codigo.etiqueta = palabra   #se guarda en la clase
                    elif cont == 1: #1 = nmonico
                        if val.isNmonico(palabra):  #Valida que el nmonico exista
                            codigo.nmonico = palabra    #se guarda en la clase 
                        else:   #Si el nmonico no existe (faltan validacione)
                            pass 
                    elif cont == 2: #2 = operador
                        codigo.operador = palabra   #se guarda en la clase
                    elif cont == 3: #3 = comentario
                        codigo.comentario = palabra #se guarda en la clase
                    else: #Otro es error (faltan validaciones)
                        pass
                    cont += 1   #contador de palabras
                val.addressMode(codigo) #Agrega a la clase el "address mode" y "object code"
                write_file(codigo, archivo.memoria)  #Envia la clase con los atributos para escribirlos en el archivo #P2 y P3
                if hasattr(codigo,"etiqueta"):
                    write_tabsim(codigo, archivo)
                if codigo.nmonico == "ORG":
                     archivo.memoria = codigo.memoria    #ORG Valor inicial de ASM 
                if hasattr(codigo, "memory"):
                     archivo.memoria = int(archivo.memoria) + int(codigo.memory)   #Se le suma a la memoria (bytes) de cada linea de codigo
                
        
        messagebox.showinfo(message=f"Codigo guardado con EXITO", title="Notification")

def write_file(codigo, memoria):
    file = open("Practica 2.txt", "a") #Abre o crea el archivo VAR para escribir ("a" - Escribe a partir del cursor)
    
    file.write(f"{str(memoria)}\n")
    if hasattr(codigo,"etiqueta"):  #Verifica que exista el atributo
        file.write(f"ETQ {str(codigo.etiqueta)}\n") 
    if hasattr(codigo,"nmonico"):   #Verifica que exista el atributo
        file.write(f"NM {str(codigo.nmonico)}\n")
    if hasattr(codigo,"operador"):  #Verifica que exista el atributo
        file.write(f"OP {str(codigo.operador)}\n")
    if hasattr(codigo,"addr_mode"):    #Verifica que exista el atributo
        file.write(f"MD {str(codigo.addr_mode)}\n")
    if hasattr(codigo,"obj1"):    #Verifica que exista el atributo
        file.write(f"OBJ {str(codigo.obj1)}")
    if hasattr(codigo,"obj2"):    #Verifica que exista el atributo
        file.write(f" {str(codigo.obj2)}\n")
    if hasattr(codigo,"memory"):    #Verifica que exista el atributo
        file.write(f"MEM {str(codigo.memory)}\n")
    if hasattr(codigo,"comentario"):    #Verifica que exista el atributo
        file.write(f"COM {str(codigo.comentario)}\n\n")
    else:
        file.write(f"\n") 

    file.close()

def write_comment(renglon):
    file = open("Practica 2.txt", "a")
    file.write(f"COM\t{renglon}\n\n")
    file.close()

def write_tabsim(codigo, archivo):
    file = open("Tabla de simbolos.txt", "a")
    file.write(f"{codigo.etiqueta}\t")
    if codigo.nmonico == "EQU":
        if codigo.operador[0] == "$":
            file.write(f"{codigo.operador}\n")
        else:
            hexa = val.convHex(codigo.operador)
            file.write(f"${hexa}\n")
    else:
        file.write(f"{archivo.memoria}\n")
    file.close()