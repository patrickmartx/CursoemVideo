# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAluguel = int(input("Quantos dias alugados?\n"))
kmRodados = float(input("Quantos kms rodados?\n"))
total = (diasAluguel * 60) + (kmRodados * 0.15)

print(f"O total a pagar é de R${total:.2f}.")