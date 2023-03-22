# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

primeiroNumero = randint(-50, 50)
segundoNumero = randint(-50, 50)
terceiroNumero = randint(-50, 50)
quartoNumero = randint(-50, 50)
quintoNumero = randint(-50, 50)
maior = 0
menor = 0

tupla = (primeiroNumero, segundoNumero, terceiroNumero, quartoNumero, quintoNumero)
for i in range(0, len(tupla)):
    if i == 0:
        maior = menor = tupla[0]
    else:
        if tupla[i] > maior:
            maior = tupla[i]
        elif tupla[i] < menor:
            menor = tupla[i]

print(f"Os valores sorteados foram: {tupla}\n"
      f"O maior valor sorteado foi: {maior}\n"
      f"O menor valor sorteado foi: {menor}")

