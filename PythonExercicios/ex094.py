# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas | B) A média de idade do grupo | C) Uma lista com todas as mulheres. | D) Uma lista com todas as pessoas com idade acima da média.
def linhas():
    return print('-=' * 30)
def formatacao():
    return f"{' ':^5}"

pessoa = []
while True:
    gente = {}
    gente['Nome'] = str(input("Nome: "))
    gente['Sexo'] = str(input("Sexo[M/F]: "))
    while gente['Sexo'] not in 'Mm' and gente['Sexo'] not in 'Ff':
        gente['Sexo'] = str(input("ERRO! Por favor, digite apenas M ou F.\nSexo[M/F]: "))
    gente['Idade'] = int(input("Idade: "))
    pessoa.append(gente.copy())

    continuar = str(input("Deseja continuar?[S/N]: "))
    if continuar in 'Nn':
        break

linhas()

print(f"A) Ao todo, temos {len(pessoa)} pessoas cadastradas.")
total = 0
for i in range(0, len(pessoa)):
    total += pessoa[i]['Idade']
media = total / len(pessoa)
print(f"B) A média de idade é de {media:.2f} anos.")
mulheres = []
for i in range(0, len(pessoa)):
    if pessoa[i]['Sexo'] in 'Ff':
        mulheres.append(pessoa[i]['Nome'])
print(f"C) As mulheres cadastradas foram: ", end='')
for i in mulheres:
    print(i, end='... ')
print()
pessoasAcimaMedia = []
for i in range(0, len(pessoa)):
    if pessoa[i]['Idade'] > media:
        pessoasAcimaMedia.append(pessoa[i])

print(f"D) Lista de pessoas que estão acima da média:")
for i in pessoasAcimaMedia:
    print(formatacao(), f"Nome = {i['Nome']}; Sexo = {i['Sexo'].upper()}; Idade = {i['Idade']}.")

linhas()
'''galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo: [M/F] ")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == 'N':
        break

linhas()
print(f"Ao todo, temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"A média de idade é de {media:.2f} anos.")
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in "Ff":
        print(f"{p['nome']} ", end='')
print()
print("Lista de pessoas que estão acima da média: ", end='')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f"\n{k} = {v} ", end='')
        print()
print('<< ENCERRADO >>')'''


