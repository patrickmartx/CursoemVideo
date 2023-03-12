# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto | à vista no cartão: 5% de desconto | em até 2x no cartão: preço normal | 3x ou mais no cartão: 20% de juros.
def interface():
    print("Qual será a forma de pagamento?")
    print("1 - Dinheiro/Cheque.\n2 - À vista no cartão.\n3 - Parcelado em até 2x.\n4 - 3x ou mais parcelas.\n")
    opcao = int(input("Digite um dos números informados: "))
    if (opcao == 1) or (opcao == 2) or (opcao == 3) or (opcao == 4):
        return opcao
    else:
        print("Opção inválida!\n")
        return interface()

def processaValor(vProd, fPag):
    if fPag == 1:
        desconto = vProd * (10/100)
        print(f"\nPagando em Dinheiro/Cheque, você ganha um desconto de 10% (R${desconto:.2f}).\nO Produto custará R${(vProd - desconto):.2f}")
    elif fPag == 2:
        desconto = vProd * (5 / 100)
        print(f"\nPagando à vista no cartão, você ganha um desconto de 5% (R${desconto:.2f}).\nO Produto custará R${(vProd - desconto):.2f}")
    elif fPag == 3:
        print(f"\nPagando em até 2x\nO Produto custará R${(vProd):.2f}")
    elif fPag == 4:
        juros = vProd * (20 / 100)
        print(f"\nPagando 3x ou mais no cartão, você paga um juros de 20%.\nO Produto custara R${(vProd + juros):.2f}")


valorProduto = float(input("Digite o valor do produto: "))
formaPagamento = interface()
valor = processaValor(valorProduto, formaPagamento)
