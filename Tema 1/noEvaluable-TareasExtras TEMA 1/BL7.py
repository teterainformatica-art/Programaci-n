lista = []
for i in range(10):
    num = int(input("dame un numero: "))
    lista.append(num)
print (lista)
min = lista[0]
max = lista[0]
for i in range(1, len(lista)):
    if lista[i]< min:
        min = lista[i]
    if lista[i]> max:
        max = lista[i]
print("minimo:", min)
print("minimo:", max)