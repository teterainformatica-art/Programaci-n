resultado = 0
n = 15
for i in range(n + 1):
    if i % 2 == 0:
        resultado = resultado + 2 * i
    else:
        resultado = resultado + 2 * i + 1
print("El resultado es:", resultado)

#resultado=0   n=15   i=0   salida
#     0         15     0       0
#     3         15     1       3
#     7         15     2       7
#     14        15     3       14
#     22        15     4       22
#     33        15     5       33
#     45        15     6
#               15     7
#               15     8
#               15     9
#               15     10
# 2 4 6 8 10 12 14