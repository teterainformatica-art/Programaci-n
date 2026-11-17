nombre = input("introduce el nombre del alummno: ").lower()
while nombre != "exit":
    nota = int(input("introduce la nota del alumno: "))
    while nota > 100 or nota < 0:
        nota = int(input("error, introduce la nota del alumno: "))
    if nota <= 49:
        print (nombre, "tiene un suspenso")
    elif nota >= 50 and nota <= 59:
        print (nombre, "tiene un suficiente")
    elif nota >= 60 and nota <= 69:
        print (nombre, "tiene un bien")
    elif nota >= 70 and nota <= 89:
        print (nombre, "tiene un notable")
    elif nota >= 90 and nota <= 100:
        print (nombre, "tiene un sobresaliente")
    nombre = input("introduce el nombre del alummno: ").lower()