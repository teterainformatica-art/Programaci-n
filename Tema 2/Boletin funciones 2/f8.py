def calcularmedia (numero, lista):
    media = float(calculartotal(lista) // numero)
    return media
    

def calculartotal(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    return suma

def calcularpares(lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)
    return pares

def calcularnegativos(lista):
    negativos = []
    for elemento in lista:
        if elemento <0:
            negativos.append(elemento)
    return negativos

lista =  []
numero = int(input("dime un numero: "))
for i in range(numero):
    numeros = int(input("suelta la pasta colegi: "))
    lista.append(numeros)

#menú
print ("====menú====")
print ("1-Devuelve la media")
print ("2-Devuelve cuántos son pares")
print ("3-Devuelve cuántos son negativos")
print ("4-Devuelve la suma de todos los números introducidos")
opcion = int(input("elige una opcion DE UNA VEZ POR DIOS NO ME PAGAN LO SUFICIENTE: "))
match opcion:
    case 1:
        media = calcularmedia(numero, lista)
        print (f"la media es {media}")

    case 2:
        pares = calcularpares(lista)
        print(pares)
    case 3:
        negativos = calcularnegativos(lista)
        print (negativos)
    case 4:
            suma = calculartotal(lista)
            print (suma)