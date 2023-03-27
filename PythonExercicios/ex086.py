# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = []
for l in range(0,3):
    linha = []
    for c in range(0,3):
        linha.append(int(input(f"Digite o valor[{l}][{c}]: ")))
    matriz.append(linha[:])

print('-=' * 30)

for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print()

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o valor [{l}][{c}]"))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()'''