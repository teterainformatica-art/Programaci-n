precio = 0
compra = 0
lista = []
while precio >= 0:
    compra += precio
    precio = float(input("introduzca el precio del producto: "))
print ("total de compra", compra,"€")