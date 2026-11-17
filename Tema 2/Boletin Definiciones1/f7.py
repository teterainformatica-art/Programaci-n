def calcularmaxmin():
    max = listanum[0]
    for i in range(1, len(listanum)):
        if listanum[i] > max:
            max = listanum[i]
    min = listanum[0]
    for i in range(1, len(listanum)):
        if listanum[i] < min:
            min = listanum[i]
    return [min, max]

listanum = []
for i in range(0,10):
    numero = int(input("dime un numero: "))
    listanum.append(numero)
max = calcularmaxmin()
min = calcularmaxmin()
#cambiar las 2 variables por 1 sola y pintarla con pos 1 y 0
print (f"{max} maximo")
print (f"{min} minimo")