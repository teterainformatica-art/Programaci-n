#calcula la media de la temperatura maxima y minima y la guarda como media
def calculatemperaturamedia(tempmax, tempmin):
    
    
            media = (tempmax + tempmin) /2
            return media


#Pide el numero de dias
dia = int(input("dime el numero día: "))
for i in range (1, dia+1):
            
            #Pide temperatura maxima y minima tantas veces como días se han dado
            tempmax = int(input("dime la temperatura maxima: "))
            tempmin = int(input("dime la temperatura minima: "))
            
            #llama al calculo de la función y lo guarda en la variable media
            media = calculatemperaturamedia(tempmax, tempmin)
            
            #Pinta la temperatura media
            print (f"La temperatura media de hoy es {media}")