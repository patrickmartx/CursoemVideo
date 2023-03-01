# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
# EX: Digite um número: 6.127 | O número 6.127 tem a parte inteira 6.
from math import trunc

numeroReal = float(input("Digite um número: "))
numeroInteiro = trunc(numeroReal)
print(f"O número {numeroReal} tem a parte inteira {numeroInteiro}.")