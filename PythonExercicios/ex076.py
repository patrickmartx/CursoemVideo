# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print("-"*40)
print(f"{'LISTAGEM DE PREÇOS': ^40}")
print("-"*40)

mercado = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for i in range(0, len(mercado)):
    if type(mercado[i]) == str:
        print(f"{mercado[i]:.<30}R$", end='')
    elif type(mercado[i]) == float:
        print(f"{mercado[i]: >8.2f}")


print("-"*40)

'''nome1 = 'Lapis'
preco1 = 1.75
nome2 = 'Borracha'
preco2 = 2.00
print(f"{nome1:.<30}R${preco1: >8.2f}")
print(f"{nome2:.<30}R${preco2: >8.2f}")'''