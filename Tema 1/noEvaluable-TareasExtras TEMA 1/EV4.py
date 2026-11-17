media = 0
edad = [14, 18, 25, 3]
altura = [1.50, 1.60, 1.92, 0.50 ]
for i in range(0, len(edad)):
    if edad[i] >= 18:
        print (altura[i],"m")
    media = media + altura[i]
media = media / len(altura)
for i in range(0, len(altura)):
    if altura[i] > media:
        print (altura[i],"m")