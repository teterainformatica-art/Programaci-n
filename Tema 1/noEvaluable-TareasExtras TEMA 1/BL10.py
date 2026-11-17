lista1 = []
lista2 = []
for i in range(15):
    numero = int(input("dime un numero: "))
    lista1.append(numero)
for i in range(len(lista1)-1, 0,-1):
    ultnum = lista1[len(lista1)]
print (ultnum)