# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime

maior = 0
menor = 0
anoAtual = datetime.now().year
for i in range(0, 7):
    anoNasc = int(input(f"Digite o ano de nascimento da {i+1}ª pessoa: "))
    if (anoAtual - anoNasc) < 18:
        menor += 1
    else:
        maior += 1
print(f"Nessa lista encontramos {menor} menores de idade {maior} maiores de idade.")
