diadelasemana = str(input("¿que dia es? "))
if diadelasemana == "lunes" or "LUNES" or "Lunes":
    print ("""LUNES
10-11 PROG 
11-11:30 Recreo
11:30-12 Progr
12-14 BBDD""")
elif diadelasemana == "sabado" or "domingo":
    print ("dia de estudio y reflexión")
else:
    print ("hoy no es tu dia")