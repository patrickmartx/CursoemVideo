# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluíndo um sistema de visualização de detalhes do aproveitamento de cada jogador.

def linhas():
    return print('-=' * 30)
def formatacao():
    return f"{' — ':^5}"

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input("Nome do jogador: ")).strip().capitalize()
    tot = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(formatacao() + f"Quantos gols na partida {c+1}: ")))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar = str(input("Deseja continuar?[S/N]: ")).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

linhas()
print('cod ', end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print('-' * 40)

while True:
    busca = int(input("Mostrar dadso de qual jogador? [999 para fechar o programa]: "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print('-' * 40)
        print(f' —— LEVANTAMENTO DO JOGADOR {time[busca]["Nome"].upper()}')
        for i, g in enumerate(time[busca]['Gols']):
            print(formatacao(), f"No jogo {i+1} fez {g} gols.")
    print('-' * 40)
print('<< VOLTE SEMPRE! >>')