bateria = int(input("¿porcentaje? "))
cargador = str(input("¿cargador conectado?" ))
if (bateria < 20) and (cargador == "no") :
    print ("activar modo ahorro de energia")
else :
    print ("no activar modo ahorro de energia")