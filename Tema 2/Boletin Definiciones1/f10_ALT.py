
#calcula las horas
def calcularhoras (segundos):
    segundosHoras = segundos // 3600
    return segundosHoras

#calcula los minutos restantes
def calcularminutosrestantes (segundos, segundoshoras):
    minutos = segundos // 60
    horas = segundosHoras * 60
    minutosrestantes = minutos - horas
    return minutosrestantes

#calcula los segundos restantes
def calcularsegundosrestantes (segundos, minutosrestantes):
    segundosrestantes = minutosrestantes * 60
    segundosrestantes = segundos - segundosrestantes
    return segundosrestantes

segundoshoras = 0
segundos = int(input("dime los segundos: "))

segundosHoras = calcularhoras(segundos)
print (f"{segundos} segundos en horas son {segundosHoras} horas")
minutosrestantes = calcularminutosrestantes(segundos, segundoshoras)
print (f"los minutos restantes son {minutosrestantes}")
segundosrestantes = calcularsegundosrestantes(segundos, minutosrestantes)
print (f"los segundos restantes son {segundosrestantes}")