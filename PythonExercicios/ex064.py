# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag)
quantidadeNumeros = 0
somaNumeros = 0
numero = int(input("Digite um número(ou 999 para terminar o programa): "))
while numero != 999:
    quantidadeNumeros += 1
    somaNumeros += numero
    numero = int(input("Digite outro número(ou 999 para terminar o programa): "))
print("Fim do programa.")
print(f"Você digitou {quantidadeNumeros} numeros e a soma de todos eles é {somaNumeros}.")