# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]Somar | [2]Multiplicar | [3]Maior | [4]Novos números | [5]Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

def interface():
    print('-=-'*20)
    print("[1] Somar\n"
          "[2] Multiplicar\n"
          "[3] Maior\n"
          "[4] Novos números\n"
          "[5] Sair do programa"
          )
    escolha = int(input("> "))
    print('-=-'*20)
    if (escolha < 1) or (escolha > 5):
        print("VALOR INVÁLIDO!")
        return interface()
    else:
        return escolha

def operacao(v1, v2, escolha):
    if escolha == 1:
        soma = v1 + v2
        return print(f"{v1} + {v2} = {soma}")
    elif escolha == 2:
        multiplicar = v1 * v2
        return print(f"{v1} X {v2} = {multiplicar}")
    elif escolha == 3:
        if v1 > v2:
            return print(f"{v1} é maior do que {v2}")
        else:
            return print(f"{v2} é maior do que {v1}")


print(("-=-" * 5), "BEM VINDOS AO NOSSO PROGRAMA!",  ("-=-" * 5))
valor1 = float(input("Escolha um valor: "))
valor2 = float(input("Escolha o segundo valor: "))
escolha = interface()
while (escolha != 5):
    if escolha != 4:
        operacao(valor1, valor2, escolha)
        escolha = interface()
    else:
        valor1 = float(input("Digite o novo primeiro valor: "))
        valor2 = novov2 = float(input("Digite o novo segundo valor: "))
        operacao(valor1, valor2, escolha)
        escolha = interface()
print(("-=-" * 5), "MUITO OBRIGADO PELO USO!",  ("-=-" * 5))


