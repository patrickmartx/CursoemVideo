# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.

distanciaViagem = float(input("Digite a distância da viagem em Km: "))
if distanciaViagem <= 200:
    preco = distanciaViagem * 0.50
else:
    preco = distanciaViagem * 0.45
print(f"O valor da viagem será R${preco:.2f}")
