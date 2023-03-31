# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro ano de nascimento de uma pessoa. Retornando um valor literal indicando se uma pessoa tem voto Negado, Opicional(Mais de 65) ou Obrigatório nas eleições.
def verificaCondicao(ano):
    """
    Verifica se a pessoa tem idade para votar ou não.
    :param ano: Ano de nascimento da pessoa
    :return: True ou False
    """
    from datetime import datetime
    anoAtual = datetime.now().year
    idade = anoAtual - anoNasc
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"


print('-'*30)
anoNasc = int(input("Em que ano você nasceu?\n> "))
a = verificaCondicao(anoNasc)
print(a)
