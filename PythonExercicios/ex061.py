# Refaça o desafio 51, lendo o primeiro termo e a razão do PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
def tratamentoPA(p, r, limite):
    print(f"1º termo: {p}")
    count = 1
    while count != limite:
        print(f"{count+1}º termo: {p+r}")
        p = p+r
        count += 1


primeiroTermo = int(input("Escreva o primeiro termo da PA: "))
razao = int(input("Escreva a razão da PA: "))
termo = int(input("Quantos termos dessa PA você deseja ver: "))
tratamentoPA(primeiroTermo, razao, termo)