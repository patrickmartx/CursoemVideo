# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input("Escreva uma frase:\n").lower().strip()
print(f"Quantas vezes aparece a letra a: {frase.count('a')}")
print(f"Posição em que 'a' aparece pela primeira vez: {frase.find('a')+1}")
print(f"Posição em que 'a' aparece pela última vez: {frase.rfind('a')+1}")

