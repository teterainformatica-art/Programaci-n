import random
piedras = int(input("Dime un numero (0-5): "))
while piedras > 5 or piedras < 0:
    piedras = int(input("Dime un numero (0-5): "))
apuesta = input("¿Par o Impar?: ").lower()
if apuesta != "par":
    apuesta = "impar"
piedramaquina = random.randint(1,5)
Apuestamaquina = random.randint(1,2)
if Apuestamaquina == 1:
    Apuestamaquina = "par"
else:
    Apuestamaquina = "impar"
suma = piedras + piedramaquina
if suma % 2 == 0:
    print ("el total es par")
    if apuesta == "par":
        print("gana el jugador")
    else:
        print("gana la maquina")
else:
    print ("el total es impar")
    if apuesta == "impar":
        print("gana el jugador")
    else:
        print("gana la maquina")