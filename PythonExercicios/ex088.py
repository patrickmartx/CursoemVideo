# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

print('-' * 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('-' * 30)

tabelas = []
quantidade = int(input("Quantos jogos você quer que eu sorteie?\n> "))
for l in range(0, quantidade):
    jogo = []
    for j in range(0, 6):
        while len(jogo) != 6:
            numero = randint(0, 60)
            if numero not in jogo:
                jogo.append(numero)

    tabelas.append(jogo[:])

print(f"{f'SORTEANDO {quantidade} JOGOS':-^30}")
for i in range(0, quantidade):
    tabelas[i].sort()
    sleep(1)
    print(f"Jogo {i+1}: {tabelas[i]}")
print(f"{'BOA SORTE':-^30}")

'''lista = list()
jogos = list()

print('-' * 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('-' * 30)
quant = int(input("Quantos jogos você quer que eu sorteie? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f" SORTEANDO {quant} JOGOS ", '-=' * 3)
for i, l in enumerate(jogos):
    sleep(1)
    print(f"Jogo {i+1}: {l}")
print('-=' * 5, '< BOA SORTE >', '-=' * 5)'''