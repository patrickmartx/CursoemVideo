def leiaDinheiro(txt):
    valor = input(txt).replace(',', '.').strip()
    while valor.isalpha() or valor.count('.') > 1 or valor.strip() == '':
        print(f"\033[0;31mVALOR INVÁLIDO! \"{valor}\" não é aceito. Insira um valor numérico.\033[m")
        valor = input(txt).replace(',', '.').strip()
    return float(valor)


def leiaInt(txt):
    num = input(txt)
    while not num.isnumeric():
        print("\033[1:31mERRO! Digite um número inteiro válido.\033[m")
        num = input(txt)
    return int(num)

