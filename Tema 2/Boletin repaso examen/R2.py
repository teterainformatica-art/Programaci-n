def crearPrimeraFila(n):
    lista = []
    for i in range (1,n+1):
        numero = i
        lista.append(numero)
    return lista

def crearTablas(lista, n, matriz):
    lista2 = []
    for i in range(1,n+1):
        for posicion in lista:
            lista2.append(posicion * i)
    matriz.append(lista2)
    print (matriz)
matriz = []
n = int(input("dime un numero:"))

lista = crearPrimeraFila(n)
print (lista)

crearTablas(lista, n, matriz)