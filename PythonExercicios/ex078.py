# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.

maior = 0
menor = 0
maioresPosicoes = []
menoresPosicoes = []

lista = []
for i in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {i+1}: ")))
    if i == 0:
        maior = lista[i]
        posicaoMaior = i
        menor = lista[i]
        posicaoMenor = i
    elif lista[i] < menor:
        menor = lista[i]
    elif lista[i] > maior:
        maior = lista[i]



print(f"Você digitou os valores: {lista}\n")
print(f"O maior valor digitado foi {maior} nas posições", end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i+1}...", end= ' ')
print(f"\nO menor valor digitado foi {menor} nas posições", end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i+1}...", end= ' ')
print('\n')