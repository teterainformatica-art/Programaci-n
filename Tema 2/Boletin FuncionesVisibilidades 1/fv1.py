def letras_en_nombre (lista):
    letra = 0
    for palabra in lista:
        for carart in palabra:
            if carart== "a":
                letra+=1
    return letra

def pintar_resultado (letra):
    print (f"tu nombre entero tiene {letra} la letra a")

lista = []
nombre = input("dime tu nombre: ")
primer_apellido = input("dime tu  primer apellido: ")
segundo_apellido = input("dime tu  segundo apellido: ")

lista.append(nombre)
lista.append(primer_apellido)
lista.append(segundo_apellido)

letra = letras_en_nombre(lista)
print (f"tu nombre entero tiene {letra} veces la letra a")