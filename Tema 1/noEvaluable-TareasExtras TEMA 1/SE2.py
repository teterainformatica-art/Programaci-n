lista = []
num = int(input("dime un numero: "))
lista.append(num)
while num != 0:
    num = int(input("dime un numero: "))
    lista.append(num)
    if lista[-2] < lista[-1]:
        print ("creciente")
    elif lista[-1] < lista[-2]:
        print ("decreciente")
    else:
        print ("desordenada")
print ("fin")

while posicion <

#te falta