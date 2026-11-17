from tkinter.messagebox import NO


total = 0
for i in range(0, 19, 2):
    if total % 2 == 0:
        total = i + total
        if i % 3 == 0:
            total = total - i
        else:
            total = total + 1
else:
	print(total+i)
print(total)

# al principio se cumplen ambos if y son 0, por lo que se quedan en 0
# en la segunda vuelta i es 2 que sumado a total = a total acaba siendo T=2 i=2 y no se cumple el segundo if, por lo que se cumple el else y total pasa a ser 3
# en la tercera vuelta total es 3 e I es 4, como no se cumple nada, se pinta el primer print=7
# en la cuarta vuelta i sigue sumando de 2 en 2 y solo se cumple el else de print asi que sigue asi hasta el final
#    Total |  i  | Salida
#1    0       0      no
#2    0       2      no
#3    2       2      no
#4    3       2      no
#5    3       4      7
#6    3       6      9
#7    3       8      11
#8    3       10     13
#9    3       12     15
#10   3       14     17
#11   3       16     19
#12   3       18     21
#13   3       20     3