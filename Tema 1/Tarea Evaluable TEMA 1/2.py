import random
nombre =""
print ("========================")
print ("sombrero seleccionador")
print ("========================")
print ("1-seleccionar casa para un alumno")
print ("2-mostrar estadisticas")
while nombre != "voldemort":
    opcion = input("elige una opción, si quieres salir, escribe la opcion 1 y di el nombre del personaje inombrable: ")
    match opcion:
        case "1":
            print("Ejecutando y seleccionando casa....")
            nombre = input("dime tu nombre: ")
            if nombre == "voldemort":
                print("Apparition, transportame a otro sitio")
            else:
                casa = random.randint(1,4)
                if casa == 1:
                    casa = "gryffindor"
                elif casa == 2:
                    casa = "slytherin"
                elif casa == 3:
                    casa = "hufflepuff"
                else: 
                    casa = "ravenclaw"
                print (f"el sombrero dice que {nombre} pertenece a {casa}...")
        case "2":
            print("Ejecutando y mostrar estadisticas")