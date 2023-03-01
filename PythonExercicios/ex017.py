# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
# O cálculo da hipotenusa é enunciado pelo Teorema de Pitágoras, que diz: “A hipotenusa é igual à raiz quadrada da soma dos catetos ao quadrado”.
from math import pow, sqrt

catetoOposto = float(input("Digite o comprimento do cateto oposto: "))
catetoAdjacente= float(input("Digite o comprimento do cateto adjacente: "))
comprimentoHipotenusa= sqrt(pow(catetoOposto, 2) + pow(catetoAdjacente, 2))

print(f"Num triângulo retângulo com comprimentos de cateto oposto {catetoOposto} e cateto adjacente {catetoAdjacente}, o comprimento da hipotenusa é {comprimentoHipotenusa:.2f}")