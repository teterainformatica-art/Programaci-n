#funcion que pide un numero y mira que el numero sea negativo y para cuando sea positivo 
def obtieneYvalidaDatosdeEntrada():
    numero = int(input("dime un numero: "))
    while numero < 0:
        numero = int(input("dime un numero: ")) 
    return numero

#devuelve lo calcuado en la funcion
numero = obtieneYvalidaDatosdeEntrada()
print (numero)