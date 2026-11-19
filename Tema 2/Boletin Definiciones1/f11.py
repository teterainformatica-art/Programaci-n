import f10

#funcion que calcula de minutos a segundos 1 minuto = 60 segundos
def minutos_segundos (tiempo):
    tiempoCalculado = tiempo * 60
    return tiempoCalculado

#funcion que calcula de horas a segundos
def horas_segundos (tiempo):
    tiempoCalculado = tiempo * 3600
    return tiempoCalculado

#funcion que calcula de minutos a horas
def minutos_horas (tiempo):
    tiempoCalculado = tiempo // 60
    return tiempoCalculado

#funcion que calcula de horas a minutos
def horas_minutos (tiempo):
    tiempoCalculado = tiempo * 60
    return tiempoCalculado

#menú
print ("====menú====")
print ("1-Convertir a segundos")
print ("2-Convertir a minutos")
print ("3-Convertir a horas")
print ("-1 para salir")

#El usuario elige una opción del menú, cuando elige una opcion del 1-3 se repite el menu
opcion = int(input("elige una opción"))
while opcion == 1 or opcion == 2 or opcion == 3:
    #Case con cada opción del menú
    match opcion:
        #Caso de pasar horas o minutos a SEGUNDOS
        case 1:
            pregunta = input("¿Quieres pasar horas o minutos?").lower()
            tiempo = int(input("introduce la cantidad:"))
            if pregunta == "minutos":
                tiempoCalculado = minutos_segundos(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} segundos")
            else:
                tiempoCalculado = horas_segundos(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} segundos")
        #Caso de pasar horas o segundos a MINUTOS        
        case 2:
            pregunta = input("¿Quieres pasar horas o segundos?").lower()
            tiempo = int(input("introduce la cantidad:"))
            if pregunta == "segundos":
                tiempoCalculado = f10.calculominutos(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} minutos")
            else:
                tiempoCalculado = horas_minutos(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} minutos")
        #Caso de pasar segundos o minutos a HORAS        
        case 3:
            pregunta = input("¿Quieres pasar segundos o minutos?").lower()
            tiempo = int(input("introduce la cantidad:"))
            if pregunta == "minutos":
                tiempoCalculado = minutos_horas(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} horas")
            else:
                tiempoCalculado = f10.calculohoras(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} horas")
        case _:
            print ("sayunara beibi")
    opcion = int(input("elige una opción"))