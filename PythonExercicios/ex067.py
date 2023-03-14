# Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário. O programa será interrompido quando o número for negativo.
def tabuada(val):
    count = 1
    print('-'* 50)
    while count <= 10:
        multiplo = val * count
        print(f"{val} X {count} = {multiplo}")
        count += 1
    print('-' * 50)


while True:
    valor = int(input("Quer ver a tabuada de qual valor? "))
    if valor < 0:
        break
    tabuada(valor)
print("Programa encerrado. VOLTE SEMPRE.")