cantidad = 0
lista = []
while cantidad < 10:
    numero = int(input("suelta un numerito por aqui: "))
    lista.append(numero)
    cantidad = cantidad + 1
print (lista)

print ("en orden inverso", lista[::-1])