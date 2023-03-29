# Faça um programa que tenha uma função chamada area(), que receba as dimenões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def interface():
    print('—=' * 20)
    print(f"{'Controle de Terrenos!':^40}")
    print('—=' * 20)
    escolha = int(input(f"{'MENU':^40}\n"
                        f"[1] Iniciar programa\n"
                        f"[2] Sair\n> "))
    while True:
        if escolha == 1 or escolha == 2:
            break
        else:
            escolha = int(input("Valor não disponível! Escolha apenas entre as opções oferecidas.\n> "))
    return escolha


def area(l, c):
    a = l * c
    print(f"A área de um terreno {l:.1f} X {c:.1f} é de {a:.1f}m².")


while True:
    validacao = interface()
    if validacao == 2:
        break
    elif validacao == 1:
        largura = float(input("Digite a largura: "))
        comprimento = float(input("Digite o comprimento: "))
        area(largura, comprimento)
    continuar = str(input("\nDigite qualquer coisa para continuar."))
    print()

print("Obrigado por usar nosso programa!")
