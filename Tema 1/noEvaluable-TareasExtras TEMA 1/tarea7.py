print ("dime un numero")
num1 = (int(input()))
print ("dime el segundo numero")
num2 = (int(input()))
if (num1 >0 ) and (num2 >0 ) :
    print ("ambos numeros son positivos")
elif (num1 <0 ) and (num2 <0 ):
    print ("ningun numero es positivo")
elif (num1 <0 ) or (num2 <0 ):
    print ("uno de los numeros es negativo")