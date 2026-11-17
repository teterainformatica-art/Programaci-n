num = (input("soy espejo y te reflejo: "))
resultado = ""
for i in range(len(num)-1,-1,-1):
    resultado += num[i]
print(resultado)

#print(num[::-1])