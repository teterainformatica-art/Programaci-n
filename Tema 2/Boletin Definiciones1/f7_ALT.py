from f6 import calcularmax
def calcularmaxmin():
    max = calcularmax
    min = listanum[0]
    for i in range(1, len(listanum)):
        if listanum[i] < min:
            min = listanum[i]
    return min, max

listanum = []
for i in range(0,10):
    numero = int(input("dime un numero: "))
    listanum.append(numero)
max = calcularmaxmin(max)
min = calcularmaxmin(min)
print (f"{max} maximo")
print (f"{min} minimo")