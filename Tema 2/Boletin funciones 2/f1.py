def pintarListaenReverse (lista):
    for i in range(0,cantidad):
        for i in range(len(lista)-1, -1, -1):
            listafinal.append(lista[i])
        return listafinal
listafinal = []
lista = []
cantidad = int(input("cuantos numeros quieres poner?"))
for i in range(0,cantidad):
    numero = int(input("introduce el numero:"))
    lista.append(numero)
listafinal = pintarListaenReverse(lista)
print (listafinal)