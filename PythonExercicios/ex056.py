# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo | Qual o nome do homem mais velho | Quantas mulheres tem menos de 20 anos.

somaIdade = 0
maiorIdadeHomem = 0
nomeMaisVelho = ''
mulheresMenosVinte = 0

for i in range(1,5):
    print('-='*20)
    print(f"{i}ª PESSOA: ")
    nome = str(input("Digite o nome: ")).strip()
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo usando M ou F: ")).strip()
    print('-='*20)
    somaIdade += idade
    if i == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
        print(idade)
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
        print(idade)
    if sexo in 'Ff' and idade < 20:
        mulheresMenosVinte += 1

mediaIdade = (somaIdade / 4)
print(f"A média das idades é de {mediaIdade}.")
print(f"O homem mais velho se chama {nomeMaisVelho} e tem {maiorIdadeHomem} anos.")
print(f"{mulheresMenosVinte} mulheres tem menos de 20 anos.")



