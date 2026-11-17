import random
nombre =""
nalu =0
c1 =0
c2 =0
c3 =0
c4 =0
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
                nalu +=1
                casa = random.randint(1,4)
                if casa == 1:
                    casa = "gryffindor"
                    c1 +=1
                elif casa == 2:
                    casa = "slytherin"
                    c2 +=1
                elif casa == 3:
                    casa = "hufflepuff"
                    c3 +=1
                else: 
                    casa = "ravenclaw"
                    c4 +=1
                print (f"el sombrero dice que {nombre} pertenece a {casa}...")
        case "2":
            if nalu > 0:
                print("Ejecutando y mostrar estadisticas")
                print(f"hay {nalu} alumnos:")
                print(f"{c1} en gryffindor")
                print(f"{c2} en slytherin")
                print(f"{c3} en hufflepuff")
                print(f"{c4} en ravenclaw")