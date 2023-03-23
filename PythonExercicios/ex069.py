# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. no final, mostre:
# a) Quantas pessoas tem mais de 18 anos. | b) Quantos homens foram cadastrados. | c) Quantas mulheres tem menos de 20 anos.

quantidadeMaiorIdade = 0
quantidadeHomens = 0
quantidadeMulheresMenoresVinte = 0
condicao = 'S'
while condicao not in 'Nn':
    print("-"*40)
    print("CADASTRE UMA PESSOA")
    print("-"*40)
    idade = int(input("Idade: "))
    if idade >= 18:
        quantidadeMaiorIdade += 1
    sexo = str(input("Sexo: [M/F] "))
    while sexo not in "Mm" and sexo not in "Ff":
        sexo = str(input("INFORMAÇÃO INVÁLIDA!\nSexo: [M/F] "))
    if sexo in "Mm":
        quantidadeHomens += 1
    elif sexo in "Ff":
        if idade <= 20:
            quantidadeMulheresMenoresVinte += 1
    print("-"*40)
    condicao = str(input("Quer continuar? [S/N] "))

print(f"Total de pessoas com mais de 18 anos: {quantidadeMaiorIdade}.\n"
      f"Ao todo, temos {quantidadeHomens} homem(ns) cadastrados.\n"
      f"E temos {quantidadeMulheresMenoresVinte} mulher(es) com menos de 20 anos.")