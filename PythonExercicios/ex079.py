# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Digite um valor | Valor adicionado com sucesso... Quer continuar? [S/N] | Valor duplicado! Não vou adicionar...

valor = []
while True:
    val = int(input("Digite um valor:\n> "))
    if valor == []:
        valor.append(val)
        print("Valor adicionado com sucesso...")
    else:
        if val in valor:
            print("Valor duplicado! Não vou adicionar...")
        else:
            valor.append(val)
            print("Valor adicionado com sucesso...")

    confirma = str(input("Quer continuar? [S/N]\n> "))
    while confirma not in 'Ss' and confirma not in 'Nn':
        confirma = str(input("CARACTERE INVÁLIDO!\n"
              "Quer continuar? [S/N]\n> "))
    if confirma in 'Nn':
        break

print(f"Você digitou os valores {sorted(valor)}")
