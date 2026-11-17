def login(usuario, contrasenia, intento):
    if intento <= 3 and usuario == "usuario1" and contrasenia == "asdasd" :
        valor = True
    else:
        valor = False
    return valor

intento = 0
usuario =""
contrasenia=""
while usuario != "usuario1" and contrasenia != "asdasd":
        usuario = input("Nombre de usuario: ")
        contrasenia = input("Contraseña: ")
        if usuario != "usuario1":
            print ("usuario incorrecto")
        if contrasenia != "asdasd":
            print ("contraseña incorrecta")
        intento+=1

valor = login(usuario, contrasenia, intento)
print (valor)