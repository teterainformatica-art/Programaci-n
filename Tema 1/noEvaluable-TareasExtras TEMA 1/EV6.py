nombre = input("introduce nombre de usuario: ")
while nombre != "usuario1":
    input("introduce un nombre valido: ")
    if nombre == "usuario1":
        contraseña = input("contraseña: ")
    while nombre != "usuario1":
        contraseña = input("contraseña incorrecta, intentelo de nuevo: ")
        if contraseña == "inicio1234":
            print ("usuario logueado correctamente")

#no funciona como debe

Nombre = str(input("Introduze tu nombre de usuario"))
contraseña = str(input("Introduze tu contraseña"))

while Nombre != "usuario1" or contraseña != "inicio1234" :
    Nombre = str(input("Introduze tu nombre de usuario"))
    contraseña = str(input("Introduze tu contraseña"))

print ("Usuario logado correctamente")