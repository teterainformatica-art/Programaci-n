lista = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sublista1 = lista[len(lista)-3 : len(lista)]
sublista2 = lista[0:len(lista)-3]
while numero>= len(lista) or numero <0:
    numero = int(input("dame un numero: "))
print (sublista1)
print (sublista2)
listasalida = sublista1 + sublista2
print (listasalida)