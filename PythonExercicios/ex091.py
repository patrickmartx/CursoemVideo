# Crie um programa onde quatro jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

formatacao = f"{' — ':^3}"

jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)
        }
ranking = list()

print('-=' * 15)
print(f"{'VALORES SORTEADOS':^30}")
print('-=' * 15)

for k, v in jogo.items():
    sleep(1)
    print(f"{k} tirou {v} no dado.")

print('-=' * 15)
print(f"{'== RANKING DOS JOGADORES ==':^30}")
print('-=' * 15)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")
print('-=' * 15)