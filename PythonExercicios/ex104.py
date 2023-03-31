# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt("Digite um n: ")
def leiaInt(txt):
    num = input(txt)
    while not num.isnumeric():
        print("\033[1:31mERRO! Digite um número inteiro válido.\033[m")
        num = input(txt)
    return int(num)


print('-'*30)
n = leiaInt("Digite um número: ")
m = leiaInt("Digite outro número: ")
print(f"Você acabou de digitar os números \33[32m{n}\033[m e \33[32m{m}\033[m.")
print(f"A soma dos dois números resulta em \33[32m{n + m}\033[m.")
