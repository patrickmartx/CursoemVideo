def leiaDinheiro(txt):
    valor = input(txt).replace(',', '.')
    while not valor.isnumeric() and not valor.replace('.', '').isnumeric():
        print("\033[0;31mVALOR INVÁLIDO! Insira um valor numérico.\033[m")
        valor = input(txt).replace(',', '.')
    return float(valor)

