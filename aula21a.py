# FUNÇÕES PARTE 2

# 1)Interative help | 2)Docstrings | 3)Argumentos opicionais | 4)Escopo de variáveis | 5)Retorno de resultados

'''
1) help() -

help()  # Abre um terminal de ajuda para dar um manual do que for pedido.
print(input.__doc__)  # Mostra a documentaão de alguma funcionalidade.
'''

'''
2) 

def contador(i, f, p):
    """
    —> Faz uma contagem e mostra na tela:
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    Função criada por Patrick de São Gonçalo.
    """
    c = i
    while c <= f:
        print(f"{c}", end='.. ')
        c += p
    print('FIM!')


help(contador)
# contador(2, 10, 2)
'''

'''
3) 

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma vale {s}")


somar(3, 2, 5)
somar(8, 4)
somar()
'''

'''
4) 

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

a = 5
teste(a)
print(f"\nA fora vale {a}")
'''

'''
5) 
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s


resp = somar(3, 2, 5)
resp2 = somar(9, 5)
resp3 = somar()

print(f"Somas = {resp}, {resp2} e {resp3}.")
'''
