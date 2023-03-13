# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

def checarFrase(frase):
    frase = frase.lower().replace(" ", "")
    fraseInversa = frase[::-1]
    if frase == fraseInversa:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo!")




frase = str(input("Digite uma frase:\n> ")).strip()
checarFrase(frase)