resultado = ""
num = int(input("dime un maldito numero: "))
if num < 3:
    for i in range(num):
        resultado += "*"
    for i in range(num):
        print (resultado)
else:
    constante = 