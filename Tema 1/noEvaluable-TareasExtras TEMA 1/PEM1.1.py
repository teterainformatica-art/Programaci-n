num = int(input("dime un numero: "))
match num:
    case 0:
        print ("el numero es cero")
    case 1:
        print ("el numero es 1")
    case 2:
        print ("el numero es 2")
    case _:
        print ("otra cosa")