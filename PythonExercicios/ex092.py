# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. se aposentar = 35 anos de contratacao
from datetime import datetime
formatacao = f"{' — ':^3}"

pessoa = {}
anoAtual = datetime.now().year
pessoa['Nome'] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
pessoa['Idade'] = anoAtual - nasc
pessoa['CTPS'] = int(input("Carteira de Trabalho (0 se não tem): "))

if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input("Ano de contratação: "))
    pessoa['Salario'] = float(input("Salário: "))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Ano de contratação'] + 35) - anoAtual)

print("=-" * 30)
for k, f in pessoa.items():
    print(formatacao, f"{k} tem o valor {f}.")
