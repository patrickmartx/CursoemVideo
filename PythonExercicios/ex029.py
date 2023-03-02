# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo qu ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidadeCarro = float(input("Digite a velocidade do carro: "))
multa = (velocidadeCarro - 80.0) * 7
if velocidadeCarro > 80.0:
    print(f"Você foi multado! Sua multa está no valor de R${multa:.2f}!")
else:
    print("Você está dirigindo com segurança!")