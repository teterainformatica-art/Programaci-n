ataques2 = 0
ataques1 = 0
ataques = 1
#Datos de brawler 1
print ("==== Brawler 1 ====")
nombre1 = input("dime el nombre del brawler :")
tipo1 = input("tipo de brawler: T (Tanque) N (normal)").upper()
while tipo1 != "T" and tipo1 != "N":
    tipo1 = input("tipo de brawler: T (Tanque) N (normal)").upper()
vida1 = int(input("¿cuanta vida tiene?:"))
daño1 = int(input("¿cuanto daño por ataque hace?:"))
#Datos de brawler 2
print ("==== brawler 2 ====")
nombre2 = input("dime el nombre del brawler:")
tipo2 = input("tipo de brawler: T (Tanque) N (normal)").upper()
while tipo2 != "T" and tipo2 != "N":
    tipo2 = input("tipo de brawler: T (Tanque) N (normal)").upper()
vida2 = int(input("¿cuanta vida tiene?:"))
daño2 = int(input("¿cuanto daño por ataque hace?:"))
#datos de los 2 brawlers
print ("==== DATOS ====")
print (f"brawler 1: {nombre1} ({tipo1}) - vida: {vida1} - daño: {daño1}")
print (f"brawler 2: {nombre2} ({tipo2}) - vida: {vida2} - daño: {daño2}")
#Pelea a ver quien gana
while vida1 > 0 or vida2 > 0:
    #daño a brawler2
    while vida2 > 0:
        if tipo2 == "T":
            vida2 = vida2 -(((daño1 * 80) // 100) * ataques)
        else:
            vida2 = vida2 - (daño1 * ataques)
        ataques1 += 1
    #daño a brawler1
    while vida1 > 0:
        if tipo1 == "T":
            vida1 = vida1 - (((daño2 * 80) // 100) * ataques) 
        else:
            vida1 = vida1 - (daño2 * ataques)
        ataques2 += 1
#ver quien gana
print (f"{nombre1} necesita {ataques1} ataques para derrotar a {nombre2}")
print (f"{nombre2} necesita {ataques2} ataques para derrotar a {nombre1}")
if ataques1 > ataques2:
    print (f"Favorito: {nombre1}")
else:
    print (f"Favorito: {nombre2}")