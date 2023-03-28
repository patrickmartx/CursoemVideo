# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
formatacao = f"{' — ':^3}"

aluno = dict()
aluno['Nome'] = str(input("Nome: ")).strip().capitalize()
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))

print('-='*30)
if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situacao'] = 'Recuperação'
else:
    aluno['Situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f"{k} é igual a {v}.")