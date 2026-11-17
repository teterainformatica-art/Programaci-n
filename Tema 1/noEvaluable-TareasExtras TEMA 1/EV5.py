num = int(input("dime un numero hulio: "))
potencia = int(input("dime la potencia: "))
n = 0
nump = 1
while num <= 0 and potencia <= 0:
        num = int(input("dime un numero positivo: "))
        potencia = int(input("dime una potencia positiva: "))
while n < potencia:
    n= n + 1
    nump = nump * num
print ("la potencia", potencia, "de", num, "es", nump)
