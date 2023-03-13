# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

def descobrePrimo(n):
    multiplos = 0
    listaMultiplos = []
    for i in range (2, n):
        if (n % i == 0):
            multiplos += 1
            listaMultiplos.append(i)
    if multiplos == 0:
        return print("É primo")
    else:
        return print(f"Não é primo, o número tem {multiplos} multiplo(s), sendo ele(s) {listaMultiplos}")


numero = int(input("Digite um número: "))
descobrePrimo(numero)