# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra | B) Quantos produtos custam mais de R$1000,00 | C) Qual é o nome do produto mais barato.

def inicio():
    print("-"*40)
    print(f"{'LOJA SUPER BARATÃO': ^40}")
    print("-"*40)

def fim():
    print(f"{' FIM DO PROGRAMA ':-^40}")

totalCompra = 0
produtosMaisMil = 0
produtoMaisBarato = 0
nomeProdutoMaisBarato = ''
count = 0

inicio()
while True:
    nomeProduto = str(input("Nome do produto: "))
    preco = float(input("Preço: R$"))

    if preco > 1000.00:
        produtosMaisMil += 1
    totalCompra += preco
    count += 1
    if count == 1:
        produtoMaisBarato = preco
        nomeProdutoMaisBarato = nomeProduto
    elif preco < produtoMaisBarato:
        produtoMaisBarato = preco
        nomeProdutoMaisBarato = nomeProduto

    condicao = str(input("Quer continuar? [S/N] "))
    if condicao not in "Ss" and condicao not in "Nn":
        condicao = str(input("OPÇÃO INVÁLIDA!\nQuer continuar? [S/N] "))
    if condicao in "Nn":
        break
fim()
print(f"O total da compra foi R${totalCompra:.2f}.\n"
      f"Temos {produtosMaisMil} produto(s) custando mais de R$1000.00.\n"
      f"O produto mais parato é o {nomeProdutoMaisBarato} e custa R${produtoMaisBarato:.2f}.")
