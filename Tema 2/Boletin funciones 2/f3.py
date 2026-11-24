def numerosQueTerminanEn3 (lista):
    lista2 = []
    for elemento in lista:
        str(elemento)
        if 3 in elemento:
            lista2.append(elemento)


lista = []
for i in range(0,10):
    numeros = int(input("dime un numero: "))
    lista.append(numeros)
numerosQueTerminanEn3(lista)