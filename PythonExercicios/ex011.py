#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²

b = float(input("Digite a largura da parede: "))
h = float(input("Digite a altura da parede: "))

a = b * h
l = a / 2

print(f"Sua parede tem a dimensão {b} X {h} e sua área é de {a}m²")
print(f"Para pintar essa parede, você precsará de {l}l de tinta.")
