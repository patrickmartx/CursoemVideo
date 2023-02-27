# Desafio implementado da aula 5 de criar um programa de soma

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
operacao = input("Qual operação quer usar? (+, -, * ou /): ")

if operacao == "+":
    print(f"Resultado: {n1 + n2}")
elif operacao == "-":
    print(f"Resultado: {n1 - n2}")
elif operacao == "*":
    print(f"Resultado: {n1 * n2}")
elif operacao == "/":
    print(f"Resultado: {n1 / n2}")
else:
    print(f"{operacao} não é um comando reconhecido.")