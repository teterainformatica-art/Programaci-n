plan = str(input("¿qué plan tienes contratado? (premium/nopremium)"))
velocidaddeconexion = int(input("¿que velocidad tiene?"))
if plan == "premium" and velocidaddeconexion > 25:
    ver4k = True
else:
    ver4k = False
print (ver4k)