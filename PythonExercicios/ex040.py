# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida
# Média abaixo de 5.0: REPROVADO | Média entre 5.0 e 6.9: RECUPERAÇÃO | Média 7.0 ou superior: APROVADO
def resultadoDaMedia(n1, n2):
    media = (n1 + n2) / 2
    if media < 5.0:
        return print(f"{cores['vermelho']}REPROVADO{cores['limpa']}")
    elif media >= 5.0 and media < 7:
        return print(f"{cores['amarelo']}RECUPERAÇÃO{cores['limpa']}")
    else:
        return print(f"{cores['verde']}APROVADO{cores['limpa']}")

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'verde': '\033[32m'
         }
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
situacao = resultadoDaMedia(nota1, nota2)