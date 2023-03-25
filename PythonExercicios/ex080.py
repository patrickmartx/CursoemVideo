# Crie um programa onde o usuário pode digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
for i in range(0, 5):
    valor = int(input("Digite um número: "))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
        print("Valor inserido no final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f"Valor inserido na posição {pos}")
                break
            pos += 1

print("-=" * 30)
print(f"Os valores digitados em ordem foram {lista}")

