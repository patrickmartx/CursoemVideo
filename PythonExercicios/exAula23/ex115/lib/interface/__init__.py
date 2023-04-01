def imprimir(txt, n=0):
    '''
    Programa que servirá como um print formatado, dando a possibilidade de inserir cores no conteúdo printado.
    :param txt: O texto do qual deseja ser formatado. Deve ser digitado entre aspas simples ou duplas.
    :param n: o código da cor que deseja inserir, sendo: 0 - sem cores | 1 - vermelho | 2 - verde | 3 - amarelo | 4 - azul | 5 - roxo | 6 - branco
    :return: Retornará um print com a cor que foi escolhida.
    '''
    c = ('\033[m',  # 0 - sem cores
         '\033[0;31m',  # 1 - vermelho
         '\033[0;32m',  # 2 - verde
         '\033[0;33m',  # 3 - amarelo
         '\033[0;34m',  # 4 - azul
         '\033[0;35m',  # 5 - roxo
         '\033[0;36m'   # 6 - branco
         )
    return print(f"{c[n]}{txt}{c[0]}")


def leiaInt(txt):
    '''
    Função cujo objetivo é filtrar o conteúdo digitado para que seja recebido apenas o que é número inteiro.
    :param txt: Texto de introdução à variável. Deve ser digitado entre aspas simples ou duplas
    :return: Numero inteiro
    '''
    while True:
        try:
            num = int(input(txt))
        except KeyboardInterrupt:
            imprimir("\nUsuário preferiu não digitar esse número.", 3)
            num = 3
            return num
        except (ValueError, TypeError):
            imprimir(f"ERRO: Por favor, digite um número inteiro válido.", 1)
        except Exception as erro:
            imprimir(f"Erro dado foi {erro.__class__}, 5")
            break
        else:
            return num


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt, n=0):
    '''
    Gera um cabeçalho para o menú.
    :param txt: O texto que ficará centralizado num espaçamento entre 42 linhas. Deve ser digitado entre aspas simples ou duplas
    :param n: o código da cor que deseja inserir, sendo: 0 - sem cores | 1 - vermelho | 2 - verde | 3 - amarelo | 4 - azul | 5 - roxo | 6 - branco
    '''
    print(linha())
    imprimir(txt.center(42), n)
    print(linha())


def menu(lista):
    '''
    Menú funcional do programa gerado através de uma lista, contendo as opções que forem geradas no programa principal.
    :param lista: Conteúdo gerado no programa principal
    :return: O conteúdo dado agora listado, separado por números e espaçamento.
    '''
    cabeçalho('MENU PRINCIPAL', 2)
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m — \033[34m{item}\033[m')
        c += 1
    opc = leiaInt("\033[33mSua opção:\033[m ")
    return opc
