# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim | Até 14 anos: Infantil | Até 19 anos: Junior | Até 20 anos: Sênior | Acima: Master
from datetime import datetime

def verificarCategoria(anoNasc):
    anoAtual = datetime.today().year
    idade = anoAtual - anoNasc
    if idade <= 9:
        return print("mirim.")
    elif idade > 9 and idade <= 14:
        return print("infantil.")
    elif idade > 14 and idade <= 19:
        return print("junior.")
    elif idade > 19 and idade <= 25:
        return print("senior.")
    else:
        return print("master.")



anoNascimento = int(input("Em que ano você nasceu?\n> "))
print("Você participa da categoria ", end='')
alistar = verificarCategoria(anoNascimento)
