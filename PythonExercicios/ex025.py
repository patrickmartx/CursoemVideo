# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Escreva um nome completo: ").strip()
if 'silva' in nome.lower():
    print("Tem Silva no nome!")
else:
    print("Não há Silva no nome!")
print(f"Tem Silva no nome?\nR: {'silva' in nome.lower()}")
