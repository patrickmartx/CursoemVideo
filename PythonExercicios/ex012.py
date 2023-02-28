#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoOriginal = float(input("Qual o preço do produto? R$"))
precoDesconto = precoOriginal - (precoOriginal * 5 /100)
print(f"O produto custava R${precoOriginal:.2f}, na promoção com desconto de 5% vai custar R${precoDesconto:.2f}.")