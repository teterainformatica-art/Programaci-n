def calculohoras (segundos):
    segundosHoras = segundos // 3600
    return segundosHoras

def calculominutos (segundos):
    segundosMinutos = segundos // 60
    return segundosMinutos

def calculotiempo (segundosParaHoras, segundosParaMinutos):
    segundostotalHoras = segundosParaHoras // 3600
    segundostotalMinutos = segundosParaMinutos // 60
    return [segundostotalHoras, segundostotalMinutos]

segundos = int(input("dime los segundos: "))

segundosHoras = calculohoras(segundos)
print (f"{segundos} en horas son {segundosHoras} horas")
segundosMinutos = calculominutos(segundos)
print (f"{segundos} en horas son {segundosMinutos} minutos")

segundosParaHoras = int(input("dime los segundos para horas: "))
segundosParaMinutos = int(input("dime los segundos para minutos: "))

segundoscalculados = segundosParaHoras + segundosParaMinutos

SegundosEnTodo = calculotiempo(segundosParaHoras, segundosParaMinutos)
print (f"Los {segundoscalculados} segundos en total son {SegundosEnTodo[0]} horas y {SegundosEnTodo[1]} minutos")