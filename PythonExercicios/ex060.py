# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

numero = int(input("Escreva um número: "))
fatorial = 1
count = numero
print(f"CALCULANDO {numero}!")
while count > 0:
    print(f"{count}", end='')
    print(" X " if count > 1 else " = ", end='')
    fatorial *= count
    count -= 1


print(f"{fatorial}.")