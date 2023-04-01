from PythonExercicios.exAula23.ex115.lib.interface import cabeçalho, imprimir


def arquivoExiste(nome):
    '''
    Checa se há um arquivo na pasta chamado pelo nome dado no programa principal.
    :param nome: nome do arquivo. Deve ser digitado entre aspas simples ou duplas
    :return: True caso exista, False caso não exista
    '''
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    '''
    Cria um arquivo na pasta onde funciona o programa principal.
    :param nome: nome do arquivo a ser criado. Deve ser digitado entre aspas simples ou duplas
    '''
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    '''
    Realiza a leitura formatada do arquivo existente.
    :param nome: Nome do arquivo a ser lido. Deve ser digitado entre aspas simples ou duplas
    '''
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabeçalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    '''
    Cadastra uma nova pessoa na arquivo selecionado.
    :param arq: Nome do arquivo. Deve ser digitado entre aspas simples ou duplas
    :param nome: Nome da pessoa a ser cadastrada. Deve ser digitado entre aspas simples ou duplas
    :param idade: Idade da pessoa a ser cadastrada
    '''
    try:
        a = open(arq, 'at')
    except:
        imprimir("Houve um erro na abertura do arquivo.", 1)
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            imprimir("Houve um erro na hora de escrever os dados!", 1)
        else:
            imprimir(f"Novo registro de {nome} adicionado.", 2)
            a.close()