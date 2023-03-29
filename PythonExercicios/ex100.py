# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep


def soma(lista):
    somaLista = 0
    for i in lista:
        if i % 2 == 0:
            somaLista += i
    print(f"Somando os valores pares de {lista}, temos {somaLista}")


def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end='')
    for i in range(0, 5):
        lista.append(randint(0, 30))
        sleep(0.3)
        print(lista[i], end=' ')
    print("PRONTO!")
    # return lista
    # soma(lista)


numeros = []
sorteia(numeros)
soma(numeros)
#numeros = sorteia(numeros)
# soma(numeros)