#Este bloque se encarga de recibir el texto del input, luego irá añadiendo un espacio por cada posicion hasta el total de la cadena
def convertirespaciado(texto):
    
        #Asignamos vacio a textoespaciado para que exista
        textoespaciado = ""
    
        #En este bucle irá añadiendo espacio en cada hueco y lo irá guardando en texto espacio asi= L" " o lo que seria letra|espacio
        for i in range(0,len(texto)):
            textoespaciado= textoespaciado+texto[i]+" "
        return textoespaciado 

#pedimos que diga una frase
texto = input("Escribe un texto: ")

#decimos que textoespaciado sea el resultado de la funcion y la pintamos
textoespaciado = convertirespaciado(texto)
print (textoespaciado)