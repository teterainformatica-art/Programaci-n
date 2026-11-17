total = 3
for i in range(0, 19, 2):
    if total % 2 == 0:
        total = i + total
    elif i % 3 == 0:
        total = 4
    else:
        total = total + 1
print(total)

#i va a contar 9 veces, hasta 18 porque va de 2 en 2 y para en 18, si llega a 20 se pasa de 19
#primero se entra en el elif, ya que el if no se cumple, una vez se cumple el elif, como total pasa a ser 4 y multiplo de 2 se cumple el if y se empieza a hacer, se suma en forma de Z hasta que total es 94 e I es 18, entonces se pinta la salida que es total, osea 94