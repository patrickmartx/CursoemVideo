# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar | Se é a hora de se alistar | Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime

def verificarAlistamento(anoNasc):
    anoAtual = datetime.today().year
    idade = anoAtual - anoNasc
    if idade < 18:
        tempoRestante = 18 - idade
        return print(f"Você ainda irá se alistar ao serviço militar. Falta(m) {tempoRestante} ano(s).")
    elif idade == 18:
        return print("Já está na hora de se alistar!")
    else:
        tempoSuperado = idade - 18
        return print(f"Já passou o tempo do alistamento à {tempoSuperado} ano(s).")


anoNascimento = int(input("Em que ano você nasceu?\n> "))
alistar = verificarAlistamento(anoNascimento)