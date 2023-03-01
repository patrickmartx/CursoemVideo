# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# EX: Ana Maria de Souza | Primeiro: Ana | Segundo: Souza

nomeCompleto = input("Digite seu nome completo: ")
nomeSeparado = nomeCompleto.split(' ')
composto = input("Seu nome é composto? (s/n): ").lower()
if composto == 's':
    print(f"Primeiro nome: {nomeSeparado[0]} {nomeSeparado[1]}\nÚltimo nome: {nomeSeparado[len(nomeSeparado) - 1]}")
elif composto == 'n':
    print(f"Primeiro nome: {nomeSeparado[0]}\nÚltimo nome: {nomeSeparado[len(nomeSeparado) - 1]}")
while composto != 's' or 'n':
    print("Comando não identificado!")
    composto = input("Seu nome é composto? (s/n): ").lower()
    if composto == 's':
        print(f"\nPrimeiro nome: {nomeSeparado[0]} {nomeSeparado[1]}\nÚltimo nome: {nomeSeparado[len(nomeSeparado) - 1]}")
        break
    elif composto == 'n':
        print(f"\nPrimeiro nome: {nomeSeparado[0]}\nÚltimo nome: {nomeSeparado[len(nomeSeparado) - 1]}")
        break