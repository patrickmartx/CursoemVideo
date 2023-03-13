# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
def tratamentoPA(p, r):
    print(f"1º termo: {p}")
    for i in range(1, 10):
        print(f"{i+1}º termo: {p+r}")
        p += r


primeiroTermo = int(input("Escreva o primeiro termo da PA: "))
razao = int(input("Escreva a razão da PA: "))
tratamentoPA(primeiroTermo, razao)