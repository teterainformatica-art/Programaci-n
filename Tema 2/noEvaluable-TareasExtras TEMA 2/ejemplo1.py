def calculasubcadena (cadena, posInicio, posFin):
    print ("llamo a calcuasubcadena")
    #imprimirla subcadena quedandome desde posInicio hasta fin incluida
    subcadena = cadena[posInicio: posFin+1]
    print(subcadena)

cadena = input("dime una cadena de 4 caracteres: ")
longitud_cadena = len(cadena)
while longitud_cadena != 4:
    cadena = input("dime una cadena de 4 caracteres: ")
    longitud_cadena = len(cadena)
#Caja de leer y validar cadena
numero = int(input("introduzca un numero: "))
if numero  % 2 == 0:
    calculasubcadena(cadena, 2, 4)
elif numero  % 3== 0:
    calculasubcadena(cadena, 1, 2)
elif numero  % 7 == 0:
    calculasubcadena(cadena, 0, 3)