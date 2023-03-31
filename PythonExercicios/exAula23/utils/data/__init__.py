def imprimir(txt, n=0):
    c = ('\033[m',  # 0 - sem cores
         '\033[0;31m',  # 1 - vermelho
         '\033[0;32m',  # 2 - verde
         '\033[0;33m',  # 3 - amarelo
         '\033[0;34m',  # 4 - azul
         '\033[0;35m',  # 5 - roxo
         '\033[0;36m'  # 6 - branco
         )
    return print(f"{c[n]}{txt}{c[0]}")


def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except KeyboardInterrupt:
            imprimir("\nUsuário preferiu não digitar esse número.", 3)
            num = 0
            return num
        except (ValueError, TypeError):
            imprimir(f"ERRO: Por favor, digite um número inteiro válido.", 1)
        except Exception as erro:
            imprimir(f"Erro dado foi {erro.__class__}, 5")
            break
        else:
            return num


def leiaFloat(txt):
    while True:
        try:
            num = input(txt).replace(',', '.').strip()
            num = float(num)
        except KeyboardInterrupt:
            imprimir("\nUsuário preferiu não digitar esse número.", 3)
            num = 0
            return num
        except (ValueError, TypeError):
            imprimir(f"ERRO: Por favor, digite um número real válido.", 1)
        except Exception as erro:
            imprimir(f"Erro dado foi {erro.__class__}")
        else:
            return num
