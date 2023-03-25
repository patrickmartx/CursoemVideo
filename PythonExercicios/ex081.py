# Crie um programa que vai ler vários números e colocar em uma lista. depois disso, mostre:
# A) Quantos números foram digitados. | B) A lista de valores ordenados de forma decrescente. | C) Se o valor 5 foi digitado ou não está na lista.

lista = []
while True:
    val = int(input("Digite um valor: "))
    lista.append(val)
    confirma = str(input("Quer continuar? [S/N] "))
    while confirma not in 'Ss' and confirma not in 'Nn':
        confirma = str(input("VALOR INVÁLIDO!\nQuer continuar? [S/N] "))
    if confirma in 'Nn':
        break

print("-=" * 30)
print(f"Você digitou {len(lista)} elementos.\n"
      f"Os valores em forma decrescente são {sorted(lista, reverse=True)}")
if 5 in lista:
    print("O valor 5 faz parte da lista.")
else:
    print("Não há valor 5 na lista.")