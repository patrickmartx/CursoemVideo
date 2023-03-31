def fatorial(num=1):
    """
    -> PROGRAMA PARA CALCULAR O FATORIAL DE UM VALOR NUMÉRICO.
    :param num: número para ser calculado o fatorial
    :return: fatorial do número dado.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"Os resultados são {f1}, {f2} e {f3}")

n = int(input("Escreva um número: "))
if par(n):
    print("É par")
else:
    print("É ímpar")
