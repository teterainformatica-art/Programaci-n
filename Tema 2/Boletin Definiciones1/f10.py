#1
def calculohoras (segundos):
    segundosHoras = segundos // 3600
    return segundosHoras

#1
def calculominutos (segundos):
    segundosMinutos = segundos // 60
    return segundosMinutos

#2
def calculotiempo (segundosParaHoras, segundosParaMinutos):
    segundostotalHoras = segundosParaHoras // 3600
    segundostotalMinutos = segundosParaMinutos // 60
    return [segundostotalHoras, segundostotalMinutos]
if __name__ == "__main__":
    #1
    segundos = int(input("dime los segundos: "))

    #1
    segundosHoras = calculohoras(segundos)
    print (f"{segundos} en horas son {segundosHoras} horas")
    segundosMinutos = calculominutos(segundos)
    print (f"{segundos} en horas son {segundosMinutos} minutos")

    #2
    segundosParaHoras = int(input("dime los segundos para horas: "))
    segundosParaMinutos = int(input("dime los segundos para minutos: "))

    #2
    segundoscalculados = segundosParaHoras + segundosParaMinutos

    #2
    SegundosEnTodo = calculotiempo(segundosParaHoras, segundosParaMinutos)
    print (f"Los {segundoscalculados} segundos en total son {SegundosEnTodo[0]} horas y {SegundosEnTodo[1]} minutos")