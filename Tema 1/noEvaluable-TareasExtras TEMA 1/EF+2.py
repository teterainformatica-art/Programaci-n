i = int(input("Ingrese un número entero: "))
for j in range(1, 6):
    cadena = ""
    for k in range(i):
        cadena = cadena + "*"
    print(cadena)
