# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

def checarFrase(frase):
    frase = frase.lower().replace(" ", "")
    fraseInversa = ''
    for letra in range(len(frase)-1, -1, -1):
        fraseInversa += frase[letra]
    if frase == fraseInversa:
        return print("É palíndromo!")
    else:
        return print("Não é palíndromo!")

'''    frase = frase.lower().replace(" ", "")
    fraseInversa = frase[::-1]
    if frase == fraseInversa:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo!")'''



frase = str(input("Digite uma frase:\n> ")).strip()
checarFrase(frase)