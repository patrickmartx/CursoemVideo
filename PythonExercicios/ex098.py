# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1 | b) de 10 até 0, de 2 em 2 | c) Uma contagem personalizada.
from time import sleep


def linha():
    return print('-=' * 20)


def contagem(inicio, fim, passo):
    if passo == 0:
        passo += 1
    if inicio < fim:
        linha()
        print(f"Contagem de {passo} em {passo}")
        for i in range(inicio, fim + 1, passo):
            #sleep(0.3)
            print(f"{i} ", end='')
        print("FIM!")
    else:
        if passo < 0:
            linha()
            print(f"Contagem de {passo*-1} em {passo*-1}")
            for i in range(inicio, fim - 1, passo):
                # sleep(0.3)
                print(f"{i} ", end='')
            print("FIM!")

        else:
            passo *= -1
            linha()
            print(f"Contagem de {passo*-1} em {passo*-1}")
            for i in range(inicio, fim-1, passo):
                #sleep(0.3)
                print(f"{i} ", end='')
            print("FIM!")



contagem(1, 10, 1)
contagem(10, 0, 2)
linha()
print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))
contagem(ini, fim, pas)