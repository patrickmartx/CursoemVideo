def metade(num=0, v=False):
    return num / 2 if v is False else moeda(num / 2)


def dobro(num=0, v=False):
    return num * 2 if not v else moeda(num * 2)


def aumentar(num=0, per=0, v=False):
    if v:
        return moeda(num + (num * (per / 100)))
    else:
        return num + (num * (per / 100))


def diminuir(num=0, per=0, v=False):
    if v:
        return moeda(num - (num * (per / 100)))
    else:
        return num - (num * (per / 100))


def moeda(num=0):
    return f"R${num:.2f}"


def resumo(num=0, aum=0, dim=0):
    print('-' * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print('-' * 30)
    print(f"Preço analisado: \t{moeda(num)}")
    print(f"Dobro do preço: \t{dobro(num, True)}")
    print(f"Metade do preço: \t{metade(num, True)}")
    print(f"{aum}% de aumento: \t{aumentar(num, aum, True):}")
    print(f"{dim}% de redução: \t{diminuir(num, dim, True)}")
    print('-' * 30)
