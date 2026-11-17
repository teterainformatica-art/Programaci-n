suma = 0
num = int(input("dime un numerijillo: "))
while num > 7:
    num = int(input("dime un numerijillo menor que el sietecillo: "))
while num < 7:
    num = num+1
    print ("por el caminito de velen va",num)
    suma = suma + num
print ("la suma de los numeros ahora es:", suma)