#empieza
#frase = input("dime una frase: ")
#sub = input("dime una inicio a buscar: ")
#valor = 0
#for i in range(0, len(sub)):
#    if sub[i] == frase[i]:
#        valor +=1
#if valor == len(sub):
#    print ("comienza por la subcadena")
#else:
#    print ("no empieza por la subcadena")

#termina
frase = input("dime una frase: ")
sub = input("dime una inicio a buscar: ")
valor = 0
for i in range(-1, -len(sub)-1, -1):
    if sub[i] == frase[i]:
        valor +=1
if valor == len(sub):
    print ("termina por la subcadena")
else:
    print ("no termina por la subcadena")