# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valroes inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def cabecalho():
    return print("-=" * 20, "\nAnalisando os valores passados...")


def maior(*vals):
    maiorValor = 0
    for i in vals:
        if i == vals[0]:
            maiorValor = i
        else:
            if i > maiorValor:
                maiorValor = i
    cabecalho()
    for i in vals:
        sleep(0.3)
        print(i, end=' ')
    print(f"Foram informados {len(vals)} valores ao todo.\n"
          f"O maior valor informado foi {maiorValor}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()