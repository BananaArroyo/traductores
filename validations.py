def addressMode(nmonico = "", operador = ""):
    object_code = objectCode(operador)

    if nmonico == "ABA":    #1
        return "INH", "18", "06", 2, ""
    elif nmonico == "ABC":  #2
        return "IDX", "1A", "E5", 2, ""
    elif nmonico == "ABY":  #3
        return "IDX", "19", "ED", 2, ""
    elif nmonico == "ADCA": #4
        if object_code == "IMM":
            return object_code, "89", "ii", 2, ""
        elif object_code == "DIR":  
            return object_code, "99", "dd", 2, ""
        elif object_code == "EXT":  
            return object_code,"B9","hh", 3 , "ll"
    elif nmonico == "ADCB": #5
        if object_code == "IMM":
            return object_code, "C9", "ii", 2, ""
        elif object_code == "DIR":
            return object_code, "D9", "dd", 2, ""
        elif object_code == "EXT":
            return object_code,"F9","hh", 3 , "ll"
    elif nmonico == "ADDA": #6
        if object_code == "IMM":
            return object_code, "8B", "ii", 2, ""
        elif object_code == "DIR":
            return object_code, "9B", "dd", 2, ""
        elif object_code == "EXT":
            return object_code,"BB","hh", 3 , "ll"
    elif nmonico == "ADDB": #7
        if object_code == "IMM":
            return object_code, "CB", "ii", 2, ""
        elif object_code == "DIR":
            return object_code, "DB", "dd", 2, ""
        elif object_code == "EXT":
            return object_code,"FB","hh", 3 , "ll"
    elif nmonico == "ADDD": #8
        if object_code == "IMM":
            return object_code, "C3", "jj", 2, "kk"
        elif object_code == "DIR":
            return object_code, "D3", "dd", 2, ""
        elif object_code == "EXT":
            return object_code,"F3","hh", 3 , "ll"
    elif nmonico == "ANDA": #9
        if object_code == "IMM":
            return object_code, "84", "ii", 2, ""
        elif object_code == "DIR":
            return object_code, "94", "dd", 2, ""
        elif object_code == "EXT":
            return object_code,"B4","hh", 3 , "ll"
    elif nmonico == "ANDB": #10
        if object_code == "IMM":
            return object_code, "C4", "ii", 2, ""
        elif object_code == "DIR":
            return object_code, "D4", "dd", 2, ""
        elif object_code == "EXT":
            return object_code,"F4","hh", 3 , "ll"
    elif nmonico == "ANDCC": #11
        return "IMM", "10", "ii", 2, ""
    elif nmonico == "ASL":  #12
        return "EXT","78","hh", 3 , "ll"
    elif nmonico == "ASLA": #13
        return "INH","4B","", 1 , ""
    elif nmonico == "ASLB": #14
        return "INH","5B","", 1 , ""
    elif nmonico == "ASLD": #15
        return "INH","59","", 1 , ""
    elif nmonico == "ASR": #16
        return "EXT","77","hh", 3 , "ll"
    elif nmonico == "ASRA": #17
        return "INH","47","", 1 , ""
    elif nmonico == "ASRB": #18
        return "INH","57","", 1 , ""
    elif nmonico == "BCLR": #19
        if object_code == "DIR":
            return object_code, "4D", "dd", 3, "mm"
        elif object_code == "EXT":
            return object_code,"1D","hh", 3 , "ll" #Falta mm obj4
    elif nmonico == "LDAA": #20
        if object_code == "IMM":
            return object_code, "86", "ii", 2, ""
        elif object_code == "DIR":
            return object_code, "96", "dd", 2, ""
        elif object_code == "EXT":
            return object_code,"b6","hh", 3 , "ll"
        elif object_code == "$$$":
            return object_code, "$", "", 0, ""
    elif nmonico == "ORG": #20
        if object_code == "$$$":
            return object_code, "$", "", 0, ""

    print("No existe nmonico")
    return "ERR","ERR","",0,""

def objectCode(operador = ""):
    print(operador[0] + " " + operador)
    if operador[0] == "#":
        return "IMM"
    if operador[0] == "$":
        return "$$$"
    elif int(operador) < 256:
        return "DIR"
    
    return "EXT"

nmominicos = ["ABA","ABX","ABY","ADCA","ADCB","ADDA","ADDB","ADDD","ANDA","ANDB","ANDCC","ASL","ASLA","ASLB","ASLD","ASR","ASRA","ASRB","BCLR","LDAA", "EQU", "ORG"]

def nmonico(palabra = ""):
    global nmominicos
    if palabra in nmominicos:
        return True
    return False

def validar_comentario(palabra = ""):
    if palabra[0] != ";":
        return False
    return True