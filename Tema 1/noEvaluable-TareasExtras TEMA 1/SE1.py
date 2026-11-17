lista = []
for i in range(0,3):
        num = int(input("dime un numero "))
        lista.append(num)
while not(lista[0] == 0 and lista[1] == 0 and lista[2] == 0): # lista[0] != 0 or lista[1] != 0 OR lista[2] != 0
    print(lista)
    if lista[0] > lista[1] > lista[2]:
        print ("orden decreciente")
    elif lista[0] < lista[1] < lista[2]:
        print ("orden creciente")
    else:
        print ("desordenado")
    lista = []
    for i in range(0,3):
        num = int(input("dime un numero "))
        lista.append(num)
print ("FIN")