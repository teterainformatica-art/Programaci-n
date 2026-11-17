import random
lista = []
for i in range(5):
    numero = random.randint(0,8)
    lista.append (numero)
print (lista)

numero = 0
multiplos = []
for i in range(20):
    multiplos.append(numero)
    numero= numero+3
    print (numero)
print(len(multiplos))