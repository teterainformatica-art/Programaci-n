anio = int(input("dime el año:"))
while anio > 0:
    if anio % 100 == 0:
        print(f"el año {anio} no es bisiesto")
        anio = int(input("dime el año:"))
    elif anio % 4 == 0 or anio % 400 == 0: 
            print(f"el año {anio} es bisiesto")
            anio = int(input("dime el año:"))
    anio = int(input("dime el año:"))