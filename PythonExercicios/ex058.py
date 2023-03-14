# Melhore o desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
import random
from time import sleep

print("=-" * 10 + " TENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO " + "-=" * 10)
numeroComputador = random.randint(0, 5)
numeroPessoa = int(input("Escreva um número de 0 a 5: "))
count = 1
print("PROCESSANDO...")
sleep(1)
while numeroPessoa != numeroComputador:
    print(f"Você errou! Continue tentando!")
    count += 1
    numeroPessoa = int(input("Escreva um número de 0 a 5: "))

if numeroComputador == numeroPessoa:
    print(f"Parabéns, você acertou o número com {count} tentativa(s)!")

