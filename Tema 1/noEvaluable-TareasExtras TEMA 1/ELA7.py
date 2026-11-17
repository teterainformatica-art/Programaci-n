cantidad = float(input("¿Cuanto dinero quiere enviar?: "))
dineroyaenviadohoy = float(input("cantidad de dinero ya enviada hoy: "))
if cantidad >= 0.50 and cantidad <= 1000:
    cantidadtotaldehoy = cantidad + dineroyaenviadohoy
    if cantidadtotaldehoy >= 2000:
        print ("ha excedido la cantidad permitida de dinero que se puede enviar en un dia")
    else:
        print ("su dinero ha sido enviado")
else:
    print ("no se puede enviar el dinero")