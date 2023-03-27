# Aprimore o desafio anterior mostrando no final:
# A) A soma de todos os valores pares digitados | B) A soma dos valores da terceira coluna. | O maior valor da segunda linha.

matriz = []
somaPares = 0
somaTerceiraColuna = 0
maiorValorSegundaLinha = 0

for l in range(0,3):
    linha = []
    for c in range(0,3):
        linha.append(int(input(f"Digite o valor para [{l}][{c}]: ")))
    matriz.append(linha[:])

for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]
        if i == 1:
            if j == 0:
                maiorValorSegundaLinha = matriz[1][0]
            else:
                if matriz[1][j] > maiorValorSegundaLinha:
                    maiorValorSegundaLinha = matriz[1][j]
        if j == 2:
            somaTerceiraColuna += matriz[i][2]

print('-=' * 30)

for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print()

print('-=' * 30)

print(f"A soma de todos os valores pares digitados: {somaPares}")
print(f"A soma dos valores da terceira coluna: {somaTerceiraColuna}")
print(f"O maior valor da segunda linha: {maiorValorSegundaLinha}")

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o valor [{l}][{c}]"))
print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f"A soma dos valores pares é {spar}")
for l in range(0, 3):
    scol += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {scol}")
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f"O maior valor da segunda linha é {mai}")'''
