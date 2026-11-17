precio = 0
compra = 0
lista = []
while precio >= 0:
    compra += precio
    precio = float(input("introduzca el precio del producto: "))
iva = compra * 0.07
print ("total de compra", iva+compra,"€")
print ("IVA añadido (7%): ", iva)