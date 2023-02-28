# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar.

carteira = float(input("Quanto dinheiro você tem disponível?\n"))
dolar = carteira / 5.20

print(f"Você pode comprar US${dolar:.2f} com R${carteira:.2f}.")