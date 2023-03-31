# ERROS, EXCESSÕES E TRATAMENTOS
# PROCURAR SOBRE ERROS DE PYTHON: Python exception list

try:
    print(x)

except NameError:
    print("não tem x")

while True:
    try:
        n = int(input("Digite um número: "))
        break
    except ValueError:
        print("Você digitou o número errado.")

a = int(input("Numerador: "))
b = int(input("Denominador: "))
try:
    r = a / b
    print(f"O resultado é {r}")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")