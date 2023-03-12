# Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
import time

def tratarEscolha():
    escolha = int(input("> "))
    if (escolha >=1) and (escolha <= 3):
        escolha = escolha - 1
        return escolha
    else:
        print(f"{cores['vermelho']}VALOR INVÁLIDO!{cores['limpa']}")
        return tratarEscolha()

def escolherVencedor(usuario, computador):
    if usuario == 0:
        if computador == 0:
            print(f"{cores['amarelo']}VOCÊS EMPATARAM{cores['limpa']}!\n"
                  f"Usuário escolheu {cores['amarelo']}{opcoes[usuario]}{cores['limpa']} e o computador escolheu {cores['amarelo']}{opcoes[computador]}{cores['limpa']}!")
        elif computador == 1:
            print(f"{cores['vermelho']}VOCÊ PERDEU!{cores['limpa']}\n"
                  f"Usuário escolheu {cores['vermelho']}{opcoes[usuario]}{cores['limpa']} e o computador escolheu {cores['verde']}{opcoes[computador]}{cores['limpa']}!")
        elif computador == 2:
            print(f"{cores['verde']}VOCÊ GANHOU!{cores['limpa']}\n"
                  f"Usuário escolheu {cores['verde']}{opcoes[usuario]}{cores['limpa']} e o computador escolheu {cores['vermelho']}{opcoes[computador]}{cores['limpa']}!")

    elif usuario == 1:
        if computador == 0:
            print(f"{cores['verde']}VOCÊ GANHOU!{cores['limpa']}\n"
                  f"Usuário escolheu {cores['verde']}{opcoes[usuario]}{cores['limpa']} e o computador escolheu {cores['vermelho']}{opcoes[computador]}{cores['limpa']}!")
        elif computador == 1:
            print(f"{cores['amarelo']}VOCÊS EMPATARAM{cores['limpa']}!\n"
                  f"Usuário escolheu {cores['amarelo']}{opcoes[usuario]}{cores['limpa']} e o computador escolheu {cores['amarelo']}{opcoes[computador]}{cores['limpa']}!")
        elif computador == 2:
            print(f"{cores['vermelho']}VOCÊ PERDEU!{cores['limpa']}\n"
                  f"Usuário escolheu {cores['vermelho']}{opcoes[usuario]}{cores['limpa']} e o computador escolheu {cores['verde']}{opcoes[computador]}{cores['limpa']}!")

    elif usuario == 2:
        if computador == 0:
            print(f"{cores['vermelho']}VOCÊ PERDEU!{cores['limpa']}\n"
                  f"Usuário escolheu {cores['vermelho']}{opcoes[usuario]}{cores['limpa']} e o computador escolheu {cores['verde']}{opcoes[computador]}{cores['limpa']}!")
        elif computador == 1:
            print(f"{cores['verde']}VOCÊ GANHOU!{cores['limpa']}\n"
                  f"Usuário escolheu {cores['verde']}{opcoes[usuario]}{cores['limpa']} e o computador escolheu {cores['vermelho']}{opcoes[computador]}{cores['limpa']}!")
        elif computador == 2:
            print(f"{cores['amarelo']}VOCÊS EMPATARAM{cores['limpa']}!\n"
                  f"Usuário escolheu {cores['amarelo']}{opcoes[usuario]}{cores['limpa']} e o computador escolheu {cores['amarelo']}{opcoes[computador]}{cores['limpa']}!")


cores = {'limpa':'\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'magenta': '\033[35m',
         'ciano': '\033[36m',
         'branco': '\033[37m',
         }

print(f"{cores['magenta']}##### JOKENPÔ #####{cores['limpa']}")
opcoes = ['Pedra', 'Papel', 'Tesoura']
print(f"Dadas as opções: 1 - {opcoes[0]}. 2 - {opcoes[1]} e 3 - {opcoes[2]}.\nEscolha a sua:")
escolhaUsuario = tratarEscolha()
escolhaComputador = randint(0,2)
print(f"Muito bem, agora o computador irá escolher.\n")
time.sleep(2)
vencedor = escolherVencedor(escolhaUsuario, escolhaComputador)



