num = input("dime un numero: ")
i=0
capicua = False
reverse = num[::-1] #guarda el numero pero al revés
if num == reverse: #compara el numero normal con el reverso
    capicua = True
else:
    capicua = False
print (capicua)
print (reverse)