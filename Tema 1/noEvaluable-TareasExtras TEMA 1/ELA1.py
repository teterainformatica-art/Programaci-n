pedido = int(input("¿cuantos euros cuesta el pedido? "))
estadocupon = (str(input("¿tiene cupon? si o no: ")))
if (pedido > 20) and (estadocupon == "si") :
    print ("tiene un 10 porciento de descuento")
else : 
    print ("no tiene descuento")