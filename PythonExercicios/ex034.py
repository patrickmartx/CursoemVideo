# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a 1.250,00, calcule um aumento de 10%. Para inferiores, o aumento é de 15%.

salario = float(input("Digite o salário do funcionário: R$"))
if salario >= 1250.00:
    novoSalario = salario + (salario * 10/100)
else:
    novoSalario = salario + (salario * 15 / 100)
print(f"Seu novo salário é R${novoSalario}")