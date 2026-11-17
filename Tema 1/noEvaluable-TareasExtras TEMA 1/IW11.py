import random
aleatorio1 = random.randint(1,10)
aleatorio2 = random.randint(1,10)
suma = aleatorio1 + aleatorio2
print (suma)
num1 = int (input("Introduce la suma: "))
while suma != num1:
    num1 = int (input("Introduce la suma: "))
print ("Enhorabuena acertaste la suma!!")
