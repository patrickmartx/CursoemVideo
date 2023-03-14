# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

numero = int(input("Escreva um número: "))
fatorial = numero
count = numero
while count != 1:
    count -= 1
    fatorial *= count
print(f"O fatorial de {numero}! é {fatorial}.")