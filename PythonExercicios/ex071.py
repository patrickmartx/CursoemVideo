# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

def operaValor(val):
    quantas50 = 0
    quantas20 = 0
    quantas10 = 0
    quantas1 = 0
    while True:
        if val % 50 == 0:
            val -= 50
            quantas50 += 1
            if val == 0:
                break
        elif val % 20 == 0:
            val -= 20
            quantas20 += 1
            if val == 0:
                break
        elif val % 10 == 0:
            val -= 10
            quantas10 += 1
            if val == 0:
                break
        elif val % 1 == 0:
            val -= 1
            quantas1 += 1
            if val == 0:
                break

    print(f"Total de {quantas50} cédulas de R$50.00\n"
          f"Total de {quantas20} cédulas de R$20.00\n"
          f"Total de {quantas10} cédulas de R$10.00\n"
          f"Total de {quantas1} cédulas de R$1.00")



print("="*40)
print(f"{'BANCO CEV': ^40}")
print("="*40)

valor = float(input("Qual valor você quer sacar? R$"))
operaValor(valor)
print("="*40)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")