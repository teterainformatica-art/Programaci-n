lista = ["gato", "perro", "conejo", "hamster", "pez", "tortuga"] 
#lista[:len(lista)] 
#lista[len(lista)-1] te devuelve el penultimo

# lista[0:len(lista)] = pinta lo que haya en la posicion que pongamos hasta el len, 
# tambien podemos poner un -2 asi : lista[0:len(lista)-2] y de esta forma contara hasta el len y luego irá para atrás segun cuanto hayanmos restado
#ejemplo: print (lista[0:len(lista)-2])

#lista[:] = pinta lo que pongamos en el rango de X:X o si lo dejamos vacio coge los valores de inicio a final
#print (lista[0:3])

#lista[-1] = pinta el hueco que pongamos empezando por el final, -1 seria el ultimo, -2 el penultimo y asi 
#ejemplo: print (lista[-1])

#lista[-len(lista)] = pinta el ultimo elemento pero al revés, osea lo que de forma normal seria el primero aqui es el ultimo
#ejemplo: print(lista[-len(lista)]) 

#lista[-len(lista):] = verdaderamente no tiene sentido el "-", ya que devuelve la ultima posición de la lista pero de forma normal (hacia la derecha)
#ejemplo: print(lista[-len(lista):]) 