# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido.

maiorPeso = 0
menorPeso = 0
for i in range(0, 5):
    peso = int(input(f"Digite o peso da {i+1}ª pessoa: "))
    if (maiorPeso == 0) and (menorPeso == 0):
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso

print(f"A pessoa com maior peso tem {maiorPeso} e a com menor peso tem {menorPeso}.")