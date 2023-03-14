# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag)
count = 0
soma = 0
while True:
    valor = int(input("Digite um valor (999 para parar): "))
    if valor == 999:
        break
    count += 1
    soma += valor
print(f"A soma dos {count} valores foi de {soma}!")