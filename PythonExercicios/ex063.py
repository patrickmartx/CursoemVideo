# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
def fibonacci(n):
    nAnterior = 0
    nProximo = 1
    count = 0
    print(nProximo, end=' ')
    while count != n-1:
        somaFib = nAnterior + nProximo
        nAnterior = nProximo
        nProximo = somaFib
        count += 1
        print(somaFib, end=' ')


numero = int(input("Escreva um número: "))
fibonacci(numero)