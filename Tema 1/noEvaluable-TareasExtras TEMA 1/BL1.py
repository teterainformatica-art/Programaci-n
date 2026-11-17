encontrado = False
posicion = 0
lista = ["gato", "perro", "conejo", "hamster", "pez", "tortuga"]
animal = input("Ingrese el nombre de un animal: ")
while not encontrado and posicion < len(lista):
    if lista [posicion] == animal:
        encontrado = True
    else:
        posicion = posicion + 1
if encontrado:
    print("El animal", animal, "está en la lista.")
else:
    print("El animal", animal, "no está en la lista.")

#Forma alternativa
#if animal in lista:
#    print("El animal", animal, "está en la lista.")
#else:
#    print("El animal", animal, "no está en la lista.")