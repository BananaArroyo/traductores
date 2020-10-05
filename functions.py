def escribir_archivo(contador=0, palabra=""):
    archivo = open("Practica 2.txt", "a")
    
    if contador == 1:   #Etiqueta
        archivo.write(f"ETI\t{palabra}\n")
    elif contador == 2: #Nmonico
        archivo.write(f"NM\t{palabra}\n")
    elif contador == 3: #Operador
        archivo.write(f"OP\t{palabra}\n")
    elif contador == 4: #Comentario
        archivo.write(f"COM\t{palabra}\n")
    else:   #Errores
        archivo.write(f"ERR\t{palabra}\n")

    archivo.close()