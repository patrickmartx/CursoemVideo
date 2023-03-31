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


def moeda(num):
    return f"R${num:.2f}"


def resumo(num, aum, dim):
    print('-' * 32)
    print(f"{'RESUMO DO VALOR':^32}")
    print('-' * 32)
    print(f"{'Preço analisado:':<20} {moeda(num)}")
    print(f"{'Dobro do preço:':<20} {dobro(num, True)}")
    print(f"{'Metade do preço:':<20} {metade(num, True)}")
    print(f"{f'{aum}% de aumento:':<20} {aumentar(num, aum, True):}")
    print(f"{f'{dim}% de redução:':<20} {diminuir(num, dim, True)}")
    print('-' * 32)
