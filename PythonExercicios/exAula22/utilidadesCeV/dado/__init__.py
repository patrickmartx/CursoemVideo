def leiaDinheiro(txt):
    valor = input(txt).replace(',', '.').strip()
    while valor.isalpha() or valor.count('.') > 1 or valor.strip() == '':
        print(f"\033[0;31mVALOR INVÁLIDO! \"{valor}\" não é aceito. Insira um valor numérico.\033[m")
        valor = input(txt).replace(',', '.').strip()
    return float(valor)

