# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# a < b + c
# b < a + c
# c < a + b

retaA = float(input("Digite o valor da reta A: "))
retaB = float(input("Digite o valor da reta B: "))
retaC = float(input("Digite o valor da reta C: "))

if retaA < retaB + retaC and retaB < retaA + retaC and retaC < retaA + retaB:
    print("É possível formar um triângulo.")
else:
    print("Não é possível formar um triângulo.")
