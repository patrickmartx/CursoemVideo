# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numero = 0
somaNumeros = 0
count = 0
media = 0
continuar = ''
while continuar != 'n':
    numero = float(input("Digite um número: "))
    somaNumeros += numero
    count += 1
    continuar = str(input("Deseja contiuar(Responda com S ou N)?\n>")).strip().lower()
    while continuar != 'n' and continuar != 's':
        print("VALOR INVÁLIDO!")
        continuar = str(input("Deseja contiuar(Responda com S ou N)?\n>")).strip().lower()

media = somaNumeros / count
print(f"Você digitou {count} números e a média deles é de {media:.2f}.")
