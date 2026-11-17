import random
jugador = 0
maquina = 0
partida = 0
jpar = 0
jimpar = 0
piedramaquina = random.randint(1,5)
Apuestamaquina = random.randint(1,2)
piedras = int(input("Dime un numero (0-5): "))
while piedras > 5 or piedras < 0:
    piedras = int(input("Dime un numero (0-5): "))
while not piedras == piedramaquina:
    apuesta = input("¿Par o Impar?: ").lower()
    if apuesta != "par":
        apuesta = "impar"
    if Apuestamaquina == 1:
        Apuestamaquina = "par"
    else:
        Apuestamaquina = "impar"
    suma = piedras + piedramaquina
    if suma % 2 == 0:
        print ("el total es par")
        if apuesta == "par":
            print("gana el jugador")
            jugador +=1
            jpar +=1
        else:
            print("gana la maquina")
            maquina +=1
    else:
        print ("el total es impar")
        if apuesta == "impar":
            print("gana el jugador")
            jugador +=1
            jimpar +=1
        else:
            print("gana la maquina")
            maquina +=1
    partida +=1
    piedras = int(input("Dime un numero (0-5): "))
    piedramaquina = random.randint(1,5)
    Apuestamaquina = random.randint(1,2)
print (f"se jugaron {partida} partidas de las cuales:")
print (f"el humano ganó {jugador} partidas")
print (f"la maquina ganó {maquina} partidas")
if jpar > jimpar:
    print (f"La elección favorita del jugador es par con {jpar} veces")
elif jpar < jimpar:
    print (f"la elección favorita del jugador es impar con {jimpar} veces")
else:
    print("el jugador no tiene elección favorita, las 2 por igual")