# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar.

carteira = float(input("Quanto dinheiro você tem disponível?\n"))
dolar = carteira / 5.20

print(f"Você pode comprar {dolar:.2f} em dólares com {carteira:.2f}R$.")