# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# EX: Digite um número: 1834 | unidade: 4, dezena: 3, centena: 8, milhar: 1

numero = input("Escreva um número (de 1 a 9999): ")
''' JEITO 1:
if len(numero) == 4:
    print(f"Unidade: {numero[3]}\nDezena: {numero[2]}\nCentena: {numero[1]}\nMilhar: {numero[0]}")
elif len(numero) == 3:
    print(f"Unidade: {numero[2]}\nDezena: {numero[1]}\nCentena: {numero[0]}\n")
elif len(numero) == 2:
    print(f"Unidade: {numero[1]}\nDezena: {numero[0]}")
elif len(numero) == 1:
    print(f"Unidade: {numero[0]}")
else:
    print("Número inválido!")
'''


''' JEITO 2
if len(numero) == 4:
    numero = int(numero)
    unidade = (numero % 10)
    dezena = (numero / 10) % 10
    centena = (numero / 100) % 10
    milhar = (numero / 1000) % 10
    print(f"Unidade: {int(unidade)}\nDezena: {int(dezena)}\nCentena: {int(centena)}\nMilhar: {int(milhar)}")
elif len(numero) == 3:
    numero = int(numero)
    unidade = (numero % 10)
    dezena = (numero / 10) % 10
    centena = (numero / 100) % 10
    print(f"Unidade: {int(unidade)}\nDezena: {int(dezena)}\nCentena: {int(centena)}")
elif len(numero) == 2:
    numero = int(numero)
    unidade = (numero % 10)
    dezena = (numero / 10) % 10
    print(f"Unidade: {int(unidade)}\nDezena: {int(dezena)}")
elif len(numero) == 1:
    numero = int(numero)
    unidade = (numero % 10)
    print(f"Unidade: {int(unidade)}")
else:
    print("Número inválido!")
'''

numero = int(numero)
unidade = (numero % 10)
dezena = (numero / 10) % 10
centena = (numero / 100) % 10
milhar = (numero / 1000) % 10
print(f"Unidade: {int(unidade)}\nDezena: {int(dezena)}\nCentena: {int(centena)}\nMilhar: {int(milhar)}")