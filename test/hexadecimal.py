decimal = 255
hexa =   hex(decimal)
print(hexa[2:])
hexa = hexa[2:]
if len(hexa) == 1:
    hexa = "0"+hexa
elif len(hexa) == 3:
    hexa = "0"+hexa

print(hexa.upper())

hexadecimal = 100
print(int(str(hexadecimal),16))