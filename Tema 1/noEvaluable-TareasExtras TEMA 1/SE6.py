dia = int(input("dime el dia: "))
mes = int(input("dime el mes:"))
anio = int(input("dime el año:"))
match mes:
    case 1:
        diap = dia
    case 2:
        diap = dia+31
    case 3:
        diap = dia+31+28
    case 4:
        diap = dia+31+28+31
    case 5:
        diap = dia+31+28+31+30
    case 6:
        diap = dia+31+28+31+30+31
    case 7:
        diap = dia+31+28+31+30+31+30
    case 8:
        diap = dia+31+28+31+30+31+30+31
    case 9:
        diap = dia+31+28+31+30+31+30+31+31
    case 10:
        diap = dia+31+28+31+30+31+30+31+31+30
    case 11:
        diap = dia+31+28+31+30+31+30+31+31+30+31
    case 12:
        diap = dia+31+28+31+30+31+30+31+31+30+31+30
print(f"han pasado {diap} dias desde el 1 de enero del {anio}")