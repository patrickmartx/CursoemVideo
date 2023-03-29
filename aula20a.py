# FUNÇÕES

def mensagem(msg):
    espaco = (len(msg)+10)
    print('-' * espaco)
    print(f"{msg:^{espaco}}")
    print('-' * espaco)


mensagem(input("Digite Uma mensagem: "))


def soma(a, b):
    print(f"a = {a}")
    print(f"b = {b}")
    s = a + b
    print(f"soma de a + b = {s}")

def somaPersonalizada(* vals):
    s = 0
    for num in vals:
        s += num
    print(f"Somando os valores {vals} temos {s}")

def contador(*num):
    print(num)
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")

def dobra(valores):
    pos = 0
    while pos < len(valores):
        valores[pos] *= 2
        pos += 1


# Programa principal
soma(8, 9)
soma(2, 1)
try:
    soma(2)
except:
    soma(2, 0)
somaPersonalizada(2, 4, 6, 8, 10)

'''contador(1, 2, 3, 4)
contador(1, 2)
contador(4, 9, 3)'''

'''vals = [2, 4, 6, 8, 10]
print(vals)
dobra(vals)
print(vals)'''