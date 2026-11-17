suma = 0
maximo = int(input("dime el maximo: "))
if maximo == 0:
    for numero in range(1, maximo+1):
        suma = suma + numero
    print ("La suma de los números del 1 al", maximo, "son:", suma)
else:
    print ("aqui no se trabaja con negativos")