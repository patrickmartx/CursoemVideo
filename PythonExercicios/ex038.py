# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior | O segundo valor é maior | Não existe valor maior, os dois são iguais.
def comparaNumero(pnum, snum):
    if pnum > snum:
        return print("O primeiro valor é maior.")
    elif snum > pnum:
        return print("O segundo valor é maior.")
    elif pnum == snum:
        return print("Não existe valor maior, os dois são iguais.")

primeiroNumero= int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))
maior = comparaNumero(primeiroNumero, segundoNumero)