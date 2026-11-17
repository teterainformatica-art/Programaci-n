#ver si numero 1 es multiplo de 2
def esmultiplo(num1, num2):

    
        resultado = False
        if num1 %num2 == 0:
            resultado = True
        return resultado


#meter los numeros
num1 = int(input("dime un numero:"))
num2 = int(input("dime otro numero:"))


#le paso los numeros y comprobamos la funcion
resultado = esmultiplo(num1, num2)
print (resultado)