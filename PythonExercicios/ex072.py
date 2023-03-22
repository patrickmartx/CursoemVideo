# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20
# Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por extenso.

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
escolha = int(input("Escreva um número de 0 a 20: "))
while (escolha < 0) or (escolha > 20):
    escolha = int(input("VALOR INVÁLIDO!\nEscreva um número de 0 a 20: "))

print(f"Você escolheu o número {numeros[escolha]}.")