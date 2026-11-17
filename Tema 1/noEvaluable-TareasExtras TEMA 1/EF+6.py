numero = int(input("Ingrese un número: "))
filafinalyprimera = numero*"*"
filaintermedia = "*" + (numero-2) * " " + "*"
for numfila in range(1, numero+1):
    if numfila == 1 or numfila == numero:
        print(filafinalyprimera)
    else:
        print(filaintermedia)