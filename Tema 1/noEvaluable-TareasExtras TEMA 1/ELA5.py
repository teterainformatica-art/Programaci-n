preciopedido = float(input("indique el precio del pedido: "))
estadoplus = str(input("¿en qué estado tiene la subscripción? (activo/inactivo): "))
if preciopedido >= 35 or estadoplus == "activo":
    print ("no se cobraran gastos de envio")
else:
    print ("se cobrarán gastos de envio")