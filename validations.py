def addressMode(codigo):

    if hasattr(codigo, "operador"):
        if codigo.operador[0] == "#":
            codigo.addr_mode = "IMM"
            codigo.addr_value = codigo.operador[1:]
        elif codigo.operador[0] == "$":
            codigo.memoria = codigo.operador[1:]
            if codigo.nmonico == "LDAA":
                decimal = int(str(codigo.memoria),16)
                if int(decimal) < 256:
                    codigo.addr_mode = "DIR"
                    codigo.addr_value = codigo.operador[1:]
                elif int(decimal) > 255:
                    codigo.addr_mode = "EXT"
                    codigo.addr_value = codigo.operador[1:]
        elif int(codigo.operador) < 256:
            codigo.addr_mode = "DIR"
            codigo.addr_value = codigo.operador
        elif int(codigo.operador) > 255:
            codigo.addr_mode = "EXT"
            codigo.addr_value = codigo.operador

        if codigo.nmonico == "EQU":   #EQU
            if hasattr(codigo, "addr_mode"):
                delattr(codigo,"addr_mode")
            pass
        if codigo.nmonico == "ORG":
            pass
        if codigo.nmonico == "END":
            pass
        if codigo.nmonico == "ABA": #1
            codigo.addr_mode = "INH"
            codigo.obj1 = "18"
            codigo.obj2 = "06"
            codigo.memory = 2

        elif codigo.nmonico == "ABC":   #2
            codigo.addr_mode = "IDX"
            codigo.obj1 = "1A"
            codigo.obj2 = "E5"
            codigo.memory = 2

        elif codigo.nmonico == "ABY":   #3
            codigo.addr_mode = "IDX"
            codigo.obj1 = "19"
            codigo.obj2 = "ED"
            codigo.memory = 2

        elif codigo.nmonico == "ADCA":  #4
            if codigo.addr_mode == "IMM":
                codigo.obj1 = "89"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "DIR":  
                codigo.obj1 = "99"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "EXT":  
                codigo.obj1 = "B9"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 3

        elif codigo.nmonico == "ADCB": #5
            if codigo.addr_mode == "IMM":
                codigo.obj1 = "C9"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "DIR":  
                codigo.obj1 = "D9"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "EXT":  
                codigo.obj1 = "F9"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 3

        elif codigo.nmonico == "ADDA": #6
            if codigo.addr_mode == "IMM":
                codigo.obj1 = "8B"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "DIR":  
                codigo.obj1 = "9B"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "EXT":  
                codigo.obj1 = "BB"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 3

        elif codigo.nmonico == "ADDB": #7
            if codigo.addr_mode == "IMM":
                codigo.obj1 = "CB"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "DIR":  
                codigo.obj1 = "DB"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "EXT":  
                codigo.obj1 = "FB"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 3

        elif codigo.nmonico == "ADDD": #8
            if codigo.addr_mode == "IMM":
                codigo.obj1 = "C3"
                codigo.obj2 = "jj kk"
                codigo.memory = 2
            elif codigo.addr_mode == "DIR":  
                codigo.obj1 = "D3"
                codigo.obj2 = "dd"
                codigo.memory = 2
            elif codigo.addr_mode == "EXT":  
                codigo.obj1 = "F3"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 3

        elif codigo.nmonico == "ANDA": #9
            if codigo.addr_mode == "IMM":
                codigo.obj1 = "84"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "DIR":  
                codigo.obj1 = "94"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "EXT":  
                codigo.obj1 = "B4"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 3

        elif codigo.nmonico == "ANDB": #10
            if codigo.addr_mode == "IMM":
                codigo.obj1 = "C4"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "DIR":  
                codigo.obj1 = "D4"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "EXT":  
                codigo.obj1 = "F4"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 3

        elif codigo.nmonico == "ANDCC": #11
            codigo.addr_mode = "IMM"
            codigo.obj1 = "10"
            codigo.obj2 = convHex(codigo.addr_value)
            codigo.memory = 2

        elif codigo.nmonico == "ASL":  #12
            codigo.addr_mode = "EXT"
            codigo.obj1 = "78"
            codigo.obj2 = convHex(codigo.addr_value)
            codigo.memory = 3

        elif codigo.nmonico == "ASLA": #13
            codigo.addr_mode = "INH"
            codigo.obj1 = "4B"
            codigo.memory = 1

        elif codigo.nmonico == "ASLB": #14
            codigo.addr_mode = "INH"
            codigo.obj1 = "5B"
            codigo.memory = 1

        elif codigo.nmonico == "ASLD": #15
            codigo.addr_mode = "INH"
            codigo.obj1 = "59"
            codigo.memory = 1

        elif codigo.nmonico == "ASR": #16
            codigo.addr_mode = "EXT"
            codigo.obj1 = "77"
            codigo.obj2 = convHex(codigo.addr_value)
            codigo.memory = 3

        elif codigo.nmonico == "ASRA": #17
            codigo.addr_mode = "INH"
            codigo.obj1 = "47"
            codigo.memory = 1

        elif codigo.nmonico == "ASRB": #18
            codigo.addr_mode = "INH"
            codigo.obj1 = "57"
            codigo.memory = 1

        elif codigo.nmonico == "BCLR": #19
            if codigo.addr_mode == "DIR":
                codigo.obj1 = "4D"
                codigo.obj2 = "dd mm"
                codigo.memory = 3
            elif codigo.addr_mode == "EXT":
                codigo.obj1 = "1D"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 3

        elif codigo.nmonico == "LDAA": #20
            if codigo.addr_mode == "IMM":
                codigo.obj1 = "86"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "DIR":  
                codigo.obj1 = "96"
                codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 2
            elif codigo.addr_mode == "EXT":  
                codigo.obj1 = "B6"
                if codigo.operador[0] == "$":
                    if len(codigo.addr_value) == 3:    #Si el hexadecimal es de 3 digito
                        codigo.addr_value = "0"+ codigo.addr_value #Se le agrega un 0 al inicio
                    codigo.obj2 = codigo.addr_value
                else:
                    codigo.obj2 = convHex(codigo.addr_value)
                codigo.memory = 3

nmonicos = ["ABA","ABX","ABY","ADCA","ADCB","ADDA","ADDB","ADDD","ANDA","ANDB","ANDCC","ASL","ASLA","ASLB","ASLD","ASR","ASRA","ASRB","BCLR","LDAA", "EQU", "ORG", "END"]

def isNmonico(palabra = ""):
    global nmonicos
    if palabra in nmonicos:
        return True
    return False

def convHex(addr_value): #Convertir a Hexadecimal
    hexa =   hex(int(addr_value))    #Convierte VAR en en hexadcimal (0xVAL)
    hexa = hexa[2:] #Se elimina "0x"

    if len(hexa) == 1:  #Si el hexadecimal es de 1 digito
        hexa = "0"+hexa #Se le agrega un 0 al inicio
    elif len(hexa) == 3:    #Si el hexadecimal es de 3 digito
        hexa = "0"+hexa #Se le agrega un 0 al inicio

    return hexa.upper() #Retorna el hexadecimal en mayusculas