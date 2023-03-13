# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

valor = 0
for i in range(1, 500):
    if (i % 3 == 0):
        valor += i
print(valor)