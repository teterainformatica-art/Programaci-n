def calcularmax():
    max = listanum[0]
    for i in range(1, len(listanum)):
        if listanum[i] > max:
            max = listanum[i]
    return max

listanum = []
for i in range(0,10):
    numero = int(input("dime un numero: "))
    listanum.append(numero)
max = calcularmax()
print (max)