# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salarioAnterior = float(input("Qual é o salário do funcionário? R$"))
novoSalario = salarioAnterior + (salarioAnterior * 15 / 100)
print(f"Um funcionário que ganhava R${salarioAnterior:.2f}, com 15% de aumento, passa a receber R${novoSalario:.2f}.")