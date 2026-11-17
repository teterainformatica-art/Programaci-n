def calculamayoresquenumero(lista, numero):
    listamayor = []
    for i in lista:
        if lista[i] > numero:
            listamayor.append(lista[i])
    return listamayor


lista = [0,1,2,3,4,5,6,7,8,9,10]
numero = int(input("dime un numero: "))

listamayor = calculamayoresquenumero(lista, numero)
print (listamayor)