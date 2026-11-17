edadusuario = int(input("edad del usuario: "))
dinero = float(input("cuanto dinero tiene: "))
bateriapatinete = int(input("cuanta bateria tiene el patinete: "))
if edadusuario >= 18 and dinero >= 1 and bateriapatinete > 15:
    desbloquearpatinete = True
else:
    desbloquearpatinete = False
print (desbloquearpatinete)