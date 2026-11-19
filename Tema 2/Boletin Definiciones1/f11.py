import f10

def minutos_segundos (tiempo):
    tiempoCalculado = tiempo * 60
    return tiempoCalculado

def horas_segundos (tiempo):
    tiempoCalculado = tiempo * 3600
    return tiempoCalculado

def minutos_horas (tiempo):
    tiempoCalculado = tiempo // 60
    return tiempoCalculado

def horas_minutos (tiempo):
    tiempoCalculado = tiempo * 60
    return tiempoCalculado

print ("====menú====")
print ("1-Convertir a segundos")
print ("2-Convertir a minutos")
print ("3-Convertir a horas")
print ("-1 para salir")
opcion = int(input("elige una opción"))
while opcion == 1 or opcion == 2 or opcion == 3:
    match opcion:
        case 1:
            pregunta = input("¿Quieres pasar horas o minutos?").lower()
            tiempo = int("introduce la cantidad:")
            if pregunta == "minutos":
                tiempoCalculado = minutos_segundos(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} segundos")
            else:
                tiempoCalculado = horas_minutos(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} segundos")
        case 2:
            pregunta = input("¿Quieres pasar horas o segundos?").lower()
            tiempo = int("introduce la cantidad:")
            if pregunta == "segundos":
                tiempoCalculado = f10.calculominutos(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} minutos")
            else:
                tiempoCalculado = horas_minutos(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} minutos")
        case 3:
            pregunta = input("¿Quieres pasar segundos o minutos?").lower()
            tiempo = int("introduce la cantidad:")
            if pregunta == "minutos":
                tiempoCalculado = minutos_horas(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} horas")
            else:
                tiempoCalculado = f10.calculohoras(tiempo)
                print (f"{tiempo} {pregunta} son {tiempoCalculado} horas")
                        