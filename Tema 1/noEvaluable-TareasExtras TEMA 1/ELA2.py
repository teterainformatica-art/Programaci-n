edad = int(input("dime tu edad "))
autorizacion = str(input("¿está autorizado? si o no: "))
if (edad >= 16) or (autorizacion == "si") :
    print ("puede comprar un juego pegi 16")
else :
    print ("no puede comprar un juego pegi 16")