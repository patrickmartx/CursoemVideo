# Faça um programa que leia algo pelo teclado  emostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

x = input("Digite algo: ")
print("Só tem espaços?\n", x.isspace())
print("É um número?\n", x.isnumeric())
print("É alfabético?\n", x.isalpha())
print("É alfanumérico?\n", x.isalnum())
print("Está em maiúsculas?\n", x.isupper())
print("Está em minúsculas?\n", x.islower())
print("Está capitalizado?\n", x.istitle())
