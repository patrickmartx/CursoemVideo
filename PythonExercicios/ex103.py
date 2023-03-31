# Faça um programa que tenha uma função chamada ficha(), que recebe dois parâmetros opicionais: O nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(n='<desconhecido>', g=0):
    if g <= 1:
        print(f"O jogador {n} fez {g} gol no campeonato.")
    else:
        print(f"O jogador {n} fez {g} gols no campeonato.")


print('-' * 30)
nome = str(input("Nome do jogador: ")).strip().capitalize()
gols = str(input("Número de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
