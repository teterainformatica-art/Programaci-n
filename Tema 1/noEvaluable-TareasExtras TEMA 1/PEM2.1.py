diadelasemana = str(input("¿que dia es? ")).upper()
match diadelasemana:
    case "LUNES":
        print ("LUNES")
        print ("10-11 PROG") 
        print ("11-11:30 Recreo")
        print ("11:30-12 Progr")
        print ("12-14 BBDD")
    case "SABADO" | "DOMINGO":
        print ("dia de estudio y reflexión")
    case _:
        print ("hoy no es tu dia")