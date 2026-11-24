def  estaOrdenadaAscendemente(lista):
    for posicion in lista:
        posicion2 = posicion -1
        if posicion > posicion2:
            ascendente = False
        else:
            ascendente = True
    print (ascendente)


lista = [1,2,3,4,5,6,2]
estaOrdenadaAscendemente(lista)