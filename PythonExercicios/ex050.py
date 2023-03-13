# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o

somaPares = 0
for i in range(0, 6):
    numero = int(input(f"Digite o {i+1}º número: "))
    if (numero % 2 == 0):
        somaPares += numero
print(somaPares)
