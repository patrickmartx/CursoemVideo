# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas | B) Uma listagem com as pessoas mais pesadas. | C) Uma listagem com as pessoas mais leves.

temporario = []
principal = []
maiorPeso = menorPeso = 0

while True:
    temporario.append(str(input("Nome: ")))
    temporario.append(float(input("Peso: ")))
    if len(principal) == 0:
        maiorPeso = menorPeso = temporario[1]
    else:
        if temporario[1] > maiorPeso:
            maiorPeso = temporario[1]
        if temporario[1] < menorPeso:
            menorPeso = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    confirma = str(input("Quer continuar? [S/N] "))
    while confirma not in 'Ss' and confirma not in 'Nn':
        confirma = str(input("VALOR INVÁLIDO!\nQuer continuar? [S/N] "))
    if confirma in 'Nn':
        break

print('-=' * 30)
print(f"Ao todo, você cadastrou {len(principal)} pessoas.")
print(f"O maior peso foi de {maiorPeso}Kg, peso de ", end='')
for p in principal:
    if p[1] == maiorPeso:
        print(f"[{p[0]}] ", end='')
print(f"\nO menor peso foi de {menorPeso}Kg, peso de ", end='')
for p in principal:
    if p[1] == menorPeso:
        print(f"[{p[0]}] ", end='')