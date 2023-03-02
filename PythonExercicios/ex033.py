# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

'''
if a > b and a > c:
    if b > c:
        print(f"Maior número: {a}\nMenor número: {c}")
    else:
        print(f"Maior número: {a}\nMenor número: {b}")
if b > a and b > c:
    if a > c:
        print(f"Maior número: {b}\nMenor número: {c}")
    else:
        print(f"Maior número: {b}\nMenor número: {a}")
if c > b and c > a:
    if b > a:
        print(f"Maior número: {c}\nMenor número: {a}")
    else:
        print(f"Maior número: {c}\nMenor número: {b}")
'''

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f"Maior número: {maior}\nMenor número: {menor}")