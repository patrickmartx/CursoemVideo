# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:
    val = int(input("Digite um número: "))
    lista.append(val)
    confirma = str(input("Quer continuar? [S/N] "))
    while confirma not in 'Ss' and confirma not in 'Nn':
        confirma = str(input("VALOR INVÁLIDO!\nQuer continuar? [S/N] "))
    if confirma in 'Nn':
        break

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print(f"A lista completa é {lista}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")