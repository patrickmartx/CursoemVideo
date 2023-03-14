# Melhore o desafio 61, perguntando se o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
primeiroTermo = int(input("Escreva o primeiro termo da PA: "))
razao = int(input("Escreva a razão da PA: "))
termo = primeiroTermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{cont}º Termo: {termo}")
        termo += razao
        cont += 1
    mais = int(input("Quantos termos você quer mostrar a mais: "))
print(f"Progressão finalizada com {total} termos.")