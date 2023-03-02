# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep

print("=-" * 10 + " TENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO " + "-=" * 10)
numeroComputador = random.randint(0, 5)
numeroPessoa = int(input("Escreva um número de 0 a 5: "))
print("PROCESSANDO...")
sleep(3)
if numeroComputador == numeroPessoa:
    print("Parabéns, você acertou o número!")
else:
    print(f"Você errou! O numero foi {numeroComputador}!")