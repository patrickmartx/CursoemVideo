# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário. Incluíndo o total de gols feitos durante o campeonato.
def linhas():
    return print('-=' * 30)
def formatacao():
    return f"{' — ':^5}"

jogador = dict()
jogador['Nome'] = str(input("Nome do jogador: ")).strip().capitalize()
quantidadePartidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
quantidadeGols = []
for i in range(0, quantidadePartidas):
    gols = int(input(formatacao() + f"Quantos gols na partida {i+1}: "))
    quantidadeGols.append(gols)
jogador['Gols'] = quantidadeGols[:]
jogador['Total'] = sum(quantidadeGols)

linhas()
print(jogador)
linhas()
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}.")
linhas()
print(f"O jogador {jogador['Nome']} teve {len(jogador['Gols'])} partidas.")
for i in range(0, len(quantidadeGols)):
    print(formatacao(), f"No jogo {i+1}, ele fez {jogador['Gols'][i]} gols.")
print(f"No total, {jogador['Nome']} fez {jogador['Total']} gols.")