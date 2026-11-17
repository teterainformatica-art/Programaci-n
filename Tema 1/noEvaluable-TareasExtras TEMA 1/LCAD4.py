num = input("dime un numero: ")
n = int(input("dime la posición: "))
while n > num:
    n = int(input("dime la posicion: "))
for i in range(0, len(num)):
    if i == n:
        print(num[i])



#cadena = input("dime algo: ").upper()
#while cadena[0] != "A":
#    cadena = input("dime algo: ")