#Funcion que comprueba las palabras de una lista y las mete en otra, si esa palabra ya está en la nueva lista no la añade
def listaSinRepetir (lista):
    lista2 = []
    for elemento in lista:
        if elemento not in lista2:
            lista2.append(elemento)
    return lista2

#Creación de la lista y sus elementos
lista = []
for i in range (5):
    texto = input("dame texto: ")
    lista.append(texto)

#Sacamos el valor de la funcion y lo imprimimos
lista2 = listaSinRepetir(lista)
print (lista2)