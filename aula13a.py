# LAÇOS DE REPETIÇÃO PARTE 1
# Laço FOR

lista = ['Patrick', 'Ana', 'João']
print(f"Sejam muito bem vindos, ", end='')
for i in range(0, len(lista)):
    if lista[i] != lista[-1]:
        print(f"{lista[i]}, ", end='')
    else:
        print(f"e {lista[i]}.")

print("\n")

inicio = int(input("Início: "))
fim = int(input("Fim: "))
passos = int(input("Passos: "))
for i in range(inicio, fim+1, passos):
    print(i)
print("Fim")

s = 0
for c in range(0, 4):
	n = int(input("Digite um valor: "))
	s += n
print(f"O somatório de todos os valores foi {s}")