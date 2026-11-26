def contar_letras_digitos(contrasenia):
    letra = 0
    digito = 0
    for elemento in contrasenia:
        if elemento == "1" or elemento == "2" or elemento == "3" or elemento == "4" or elemento == "5" or elemento == "6" or elemento == "7" or elemento == "8" or elemento == "9" or elemento == "0":
            digito = digito +1
        else:
            letra = letra +1
    return [letra, digito]

def es_segura(contrasenia):
    lista = contar_letras_digitos(contrasenia)
    if lista[0] >= 8 and lista[1] >= 2:
        es_segura = True
    else:
        es_segura = False
    return es_segura

def ocultar(contrasenia):
    asterisco = " "
    for i in range(len(contrasenia)-2):
        asterisco = asterisco + "*" 
    cadena = contrasenia[0] + asterisco + contrasenia[-1]
    return cadena



contrasenia = input("dime la contraseña: ")

lista = contar_letras_digitos(contrasenia)
print (f"la contraseña tiene {lista[0]} letras")
print (f"la contraseña tiene {lista[1]} numeros")
print ("===================================")
es_segura = es_segura(contrasenia)
print (es_segura)
print ("===================================")
primeraYultima = ocultar(contrasenia)
print (f"la primera y ultima letra son {primeraYultima}")

