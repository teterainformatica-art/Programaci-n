espremium = str(input("¿es usuario premium? (si o no): "))
tiemposinanuncios = int(input("¿cuantos minutos lleva sin saltar un anuncio? "))
if (espremium == "no") and (tiemposinanuncios >=30):
    print ("reproduce 50 anuncios")
# si es usuario premium no pasará nada
