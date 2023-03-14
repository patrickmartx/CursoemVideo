# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
def fibonacci(n):
    nAnterior = 0
    nProximo = 1
    count = 2
    print(f"{nAnterior} -> {nProximo}", end='')
    while count != n:
        somaFib = nAnterior + nProximo
        nAnterior = nProximo
        nProximo = somaFib
        count += 1
        print(f" -> {somaFib}", end='')


numero = int(input("Escreva um número: "))
fibonacci(numero)
print("\nFIM DO PROGRAMA.")
