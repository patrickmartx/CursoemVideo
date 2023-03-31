def leiaDinheiro(txt):
    valor = input(txt).replace(',', '.')
    while valor.isalpha() or valor.count('.') > 1:
        print(f"\033[0;31mVALOR INVÁLIDO! \"{valor}\" é aceito. Insira um valor numérico.\033[m")
        valor = input(txt).replace(',', '.')
    return float(valor)

