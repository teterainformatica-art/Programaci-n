import random
lista1 = []
cantidad1 = 0
lista2 = []
lista3 = []
while cantidad1 < 20:
    numrandom = random.randint(0,100)
    lista1.append(numrandom)
    numrandom2 = numrandom * numrandom
    lista2.append(numrandom2)
    numrandom3 = numrandom * numrandom * numrandom
    lista3.append(numrandom3)
    cantidad1 = cantidad1 + 1
print (lista1)
print ("Numeros al cuadrado de lista 1", lista2)
print ("Numeros al cubo de lista 1", lista3)

listacolumna = []
for i in range(0,len(lista1)):
    listacolumna=[]
    listacolumna.append([lista1[i]])
    listacolumna.append([lista2[i]])
    listacolumna.append([lista3[i]])
    print (listacolumna)