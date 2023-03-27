# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

'''pares = []
impares = []

for i in range(0, 7):
    numero = int(input(f"Digite o {i+1} valor: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

numeros = [pares[:], impares[:]]
pares.clear()
impares.clear()


print(f"Valores pares digitados: {sorted(numeros[0])}\n"
      f"Valores ímpares digitados: {sorted(numeros[1])}")'''

numeros = [[], []]

valor = 0
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {numeros[0]}\n'
      f'Os valores ímpares digitados foram: {numeros[1]}')