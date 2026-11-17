numpartida = 0
trofeos = 0
brawler = 0
#menu
print ("===== BRAWL STARS REGISTRO =====")
print ("1.Guardar datos del brawler")
print ("2.Registrar partida")
print ("3. Mostrar resumen")
print ("4.Terminar programa")
opcion = input("Selecciona una opción: ")
while opcion == "1" or opcion == "2"or opcion == "3":
    match opcion:
        #Guardar datos de brawler
        case "1":
            print("Guardando datos de un brawler:")
            nombre = input("dime el nombre del brawler: ")
            rareza = input("dime la rareza del brawler C (Común) R (Rara) E (Épico) L (Legendario): ").upper()
            while rareza != "C" and rareza != "R" and rareza != "E" and rareza != "L":
                rareza = input("dime la rareza del brawler C (Común) R (Rara) E (Épico) L (Legendario): ").upper()
            trofeostotales = int(input("cantidad de trofeos iniciales: "))
            print (f"Registrados los datos del brawler {nombre}")
            brawler = 1
        #Guardar resultado de partida    
        case "2":
            print("registrando:")
            mododejuego = input("introduce el modo de juego G (atrapagemas) B (Balón brawl) N (noqueo) S (supervivencia):").upper()
            while mododejuego != "G" and mododejuego != "B" and mododejuego != "N" and mododejuego != "S":
                mododejuego = input("introduce el modo de juego G (atrapagemas) B (Balón brawl) N (noqueo) S (supervivencia):").upper()
            #Si el usuario ha jugado cualquier modo que no es supervivencia    
            if mododejuego == "G" or mododejuego == "B" or mododejuego == "N":    
                resultadop = input("introduce el resultado de la partida V (victoria) D (derrota) E (empate): ").upper()
                if resultadop == "V":
                    trofeos = trofeos + 10
                elif resultadop == "D":
                    trofeos = trofeos - 5
            #si el usuario ha jugado supervivencia        
            else:
                posicion = int(input("¿En que posición quedaste en supervivencia?: "))
                trofeos = 12 - 2 * posicion
            trofeostotales = trofeostotales + trofeos
            print("Resultado:")
            print(f"el brawler {nombre} ha conseguido {trofeos} trofeos en esta partida, quedando su total de trofeos a {trofeostotales}")
            numpartida +=1
        case "3":
            if brawler == 1:
                print("Resumiendo:")
                print(f"El brawler {nombre} de rareza {rareza} ha jugado {numpartida} partidas con un total de {trofeostotales} trofeos")
            else:
                print("Primero debes guardar los datos de un brawler")
    opcion = input("Selecciona una opción: ")
print ("adios")