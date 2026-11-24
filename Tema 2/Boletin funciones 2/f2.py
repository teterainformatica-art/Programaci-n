#1-Funcion para llamar pintar las sub-listas en filas
def pintarLista(lista):
    for posicion in lista:
        print(posicion)

#2-Funcion para pintar las sub-listas por filas en orden inverso
def pintarListaInversa(lista):
    for posicion in lista[::-1]:
        print(posicion)
        return lista
#3-Funcion para pintar las sub-listas por filas al revés
def pintarSubListaReves(lista):
    for posicion in lista:
        print(posicion[::-1])
        

def imprimeMatrizInvertida(lista):
    hola = pintarListaInversa(lista)
    holafinal = pintarSubListaReves(hola)
    pintarLista(holafinal)
          


l1 = [8, 1, 6]
l2 = [3, 5, 7]
l3 = [4, 9, 2]
lista = [l1, l2, l3]
#1
pintarLista(lista)
print ("=========")
#2
pintarListaInversa(lista)
print ("=========")
#3
pintarSubListaReves(lista)
print ("=========")
imprimeMatrizInvertida(lista)