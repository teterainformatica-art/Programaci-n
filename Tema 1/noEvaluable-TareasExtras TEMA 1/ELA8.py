estadocuota = str(input("¿tiene la cuota activa? (si/no): "))
plazareservada = str(input("¿tiene plaza reservada? (si/no): "))
if estadocuota == "si" and plazareservada == "si" :
    hora = int(input("¿que hora es?: "))
    if hora >= 7 and hora < 22:
     print ("puede ir y entrar")
    else:
        print ("está cerrado")
else:
    print("no puede entrar")