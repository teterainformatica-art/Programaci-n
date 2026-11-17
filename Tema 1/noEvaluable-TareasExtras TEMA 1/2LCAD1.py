print ("MENÚ")
print ("=============")
print ("Introduzca 1 si desea ver caracter a caracter")
print ("Introduzca 2 si desea ver el porcentaje de veces que aparece una cadena")
print ("Introduzca exit si desea salir")
print ("=============")
valor = 0
num = input("Elige una opción: ")
while num != "exit":
    match num:
        case "1":
            cadena = input("dime algo: ")
            for i in range(len(cadena)-1,-1,-1):
                print(cadena[i])
        case "2":
            frase = input("dime una frase: ")
            letra = input("dime una letra a buscar: ")
            while letra not in frase:
                print (f"la frase no contiene la letra {letra}")
                letra = input("dime una letra a buscar: ")
            for i in range(0, len(frase)):
                if frase[i] == letra:
                    valor += 1
            resultado = (valor * len(frase)) / 100
            print (resultado)
        case _:
            print ("Opción no encontrada")
    num = input("Elige una opción: ")
print ("Adios")