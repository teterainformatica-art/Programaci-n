ataques2 = 0
ataques1 = 0
ataques = 1
ronda1 = 1
ronda2 = 1
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
dañoriginal1 = daño2
dañoriginal2 = daño2
vida1restante = vida1
vida2restante = vida2
#hay un error con los while de la comprobación de la vida restante
#Pelea a ver quien gana
while vida1 > 0 or vida2 > 0:
    #daño a brawler2
    while vida2restante > 0:
        daño1 = dañoriginal1    
        if ronda1 % 3 == 0:
            daño1 = daño1 * 2
        if tipo2 == "T":
            vida2restante = vida2 -(((daño1 * 80) // 100) * ataques)
        else:
            vida2restante = vida2 - (daño1 * ataques)
        ataques1 += 1
        ronda1 +=1
    #daño a brawler1
    while vida1restante > 0:
        daño2 = dañoriginal2
        if ronda2 % 3 == 0:
            daño2 = daño2 * 2
        if tipo1 == "T":
            vida1restante = vida1 - (((daño2 * 80) // 100) * ataques) 
        else:
            vida1restante = vida1 - (daño2 * ataques)
        ataques2 += 1
        ronda2 +=1
resultado1 = (vida1restante * vida1) // 100
resultado2 = (vida2restante * vida2) // 100
#quien gana
if vida1 < vida2:
    print (f"gana {nombre2} en la ronda {ronda2} con {resultado2}% ")
if vida2 < vida1:
    print (f"gana {nombre1} en la ronda {ronda1} con {resultado1}%")
if vida1 == vida2:
    print ("ambos pierden")

