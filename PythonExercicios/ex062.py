# Melhore o desafio 61, perguntando se o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
def tratamentoPA(p, r, limite):
    print(f"1º termo: {p}")
    count = 1
    while count != limite:
        print(f"{count+1}º termo: {p+r}")
        p = p+r
        count += 1


termo = int(input("Quantos termos dessa PA você deseja ver: "))
while termo != 0:
    primeiroTermo = int(input("Escreva o primeiro termo da PA: "))
    razao = int(input("Escreva a razão da PA: "))
    tratamentoPA(primeiroTermo, razao, termo)
    termo = int(input("Quantos termos dessa PA você deseja ver: "))
print("FIM DO PROGRAMA")