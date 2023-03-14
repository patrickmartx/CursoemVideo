# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite o sexo usando M ou F: ")).strip()
while (sexo not in 'Mm') and (sexo not in 'Ff'):
    print("VALOR INVÁLIDO!")
    sexo = str(input("Digite o sexo usando M ou F: ")).strip()