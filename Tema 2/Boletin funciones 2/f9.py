import random
#CREAR UNA LISTA CON NUMEROS RANDOMS 
def crearnumerosRandom():
    lista = []
    for i in range(100):
        numero = random.randint(0,1000)
        lista.append(numero)
    return lista

#MENU
def menu(lista):
    print ("====menú====")
    print ("1-Conoce el mayor")
    print ("2-Conoce el menor")
    print ("3-obtiene la suma total")
    print ("4-Sustituir el valor de un elemento por otro número introducido por teclado")
    print ("5-Mostrar todos los números")
    opcion = int(input("espabila chaval que te va a comer la vida, elige una opción: "))
    match opcion:
        case 1:
            elementomayor = calcularmayor(lista)
            print (elementomayor)
        case 2:
            elementomenor = calcularmenor(lista)
            print (elementomenor)
        case 3:
            suma = sumatotal(lista)
            print (suma)
        case 4:
            sobreescribir(lista)
        case 5:
            print (lista)
    return opcion

#TE MUESTRA EL NUMERO MAS GRANDE DE LA LISTA PARA QUE VEAS QUIEN MANDA
def calcularmayor(lista):
    elementomayor = 0
    for elemento in lista:
        if elemento > elementomayor:
            elementomayor = elemento  
    return elementomayor

#TE MUESTRA EL NUMERO MAS CHICO DE LA LISTA PARA QUE VEAS QUIEN NO MANDA
def calcularmenor(lista):
    elementomenor = 99
    for elemento in lista:
        if elemento < elementomenor:
            elementomenor = elemento
    return elementomenor

#TE MUESTRA LA SUMA TOTAL DE TOOOOODOS LOOOS NUMERROOOOOOOS
def sumatotal(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    return suma

#SE CARGA UN NUMERO QUE TU DIGAS Y PONE OTRO, COMO EL GOBIERNO
def sobreescribir(lista):
    valorbuscado = int(input("dime el valor que quieres sobreescribir"))
    valor = int(input("dime lo que quieres poner"))
    for valorbuscado in lista:
        if valorbuscado in lista:
            valorbuscado = valor
    print (lista)


#EMPIEZA EL PROGRAMA Y LLAMA A LA CREACION DE NUMEROS ALEATORIOS Y 
lista = crearnumerosRandom()
opcion = ""
while opcion != 0:
    opcion = menu(lista)
