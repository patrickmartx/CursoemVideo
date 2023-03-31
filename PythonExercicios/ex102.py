# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    """
    Um programa que calcula o fatorial de um número dado.
    :param num: Número do qual será dado o fatorial.
    :param show: Caso seja True, mostrará a etapa do cálculo da fatorial.
    :return: O resultado do fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f"{c} X ", end='')
            else:
                print(f"{c} = ", end='')
    return print(f)


num = int(input("Escreva um número para fazer seu fatorial: "))
val = str(input("Quer ver o processo? [S/N]")).upper()[0]
while val != 'N' and val != 'S':
    val = str(input("VALOR INVÁLIDO!\nQuer ver o processo? [S/N]")).upper()[0]
if val == "S":
    fatorial(num, show=True)
else:
    fatorial(num)
