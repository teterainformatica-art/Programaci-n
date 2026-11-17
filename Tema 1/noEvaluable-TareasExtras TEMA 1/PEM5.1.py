mes = int(input("dime el mes: "))
dia = int(input("dime que dia es"))
match mes:
    case 1|2|3:
        print ("estacion = invierno")
        if mes == 3 and dia >20:
            print ("primavera")
        else:
            print ("invierno")
    case 4|5|6:
        print ("estacion = primavera")
        if mes == 6 and dia >20:
            print ("verano")
        else:
            print ("primavera")
    case 7|8|9:
        print ("estacion = verano")
        if dia >20:
            print ("otoño")
        else:
            print ("verano")
    case 10|11|12:
        print ("estacion = otoño")
        if dia >20:
            print ("otoño")
        else:
            print ("invierno")
    case _:
        print ("no es un mes valido, aplicatela")