    
def addressMode(nmonico = "", operador = ""):

    object_code = objectCode(operador)

    if nmonico == "ABA":
        return "INH", "18", "06", 2
    elif nmonico == "ABC":
        return "IDX", "1A", "E5", 2
    elif nmonico == "ABY":
        return "IDX", "19", "ED", 2
    elif nmonico == "ADCA":
        if object_code == "IMM":
            return object_code, "89", "ii", 2
        elif object_code == "DIR":
            return object_code, "99", "dd", 2
        elif object_code == "EXT":
            return object_code,"B9","hh", 3
    
    print("No existe nmonico")
    return "","","",0

def objectCode(operador = ""):
    if operador[0] == "#":
        return "IMM"
    elif int(operador) < 256:
        return "DIR"
    
    return "EXT"