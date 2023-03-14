# Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando o jogador PERDER. Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print("=-" * 15 +
      "\nVAMOS JOGAR PAR OU ÍMPAR\n" +
      "=-" * 15)

vitoriasConsecutivas = 0
while True:
    jogador = int(input("Digite um valor: "))
    computador = randint(0, 50)
    escolha = str(input("Par im Ímpar? [P/I} ")).strip()
    while escolha not in "Pp" and escolha not in "Ii":
        print("VALOR INVÁLIDO!")
        escolha = str(input("Par im Ímpar? [P/I} ")).strip()
    soma = jogador + computador
    if (soma % 2 == 0):
        if escolha in "Pp":
            print((f"-" * 30) +
                  f"\nVocê jogou {jogador} e o computador {computador}. Total deu {soma} DEU PAR\n" +
                  ("-" * 30))
            print("Você VENCEU!\nVamos jogar novamente...\n" +
                  ("=-" * 15))
            vitoriasConsecutivas += 1
        else:
            print((f"-" * 30) +
                  f"\nVocê jogou {jogador} e o computador {computador}. Total deu {soma} DEU PAR\n" +
                  ("-" * 30))
            print("Você PERDEU!\n" +
                  ("=-" * 15))
            break
    else:
        if escolha in "Pp":
            print((f"-" * 30) +
                  f"\nVocê jogou {jogador} e o computador {computador}. Total deu {soma} DEU IMPAR\n" +
                  ("-" * 30))
            print("Você PERDEU!\n" +
                  ("=-" * 15))
            break
        else:
            print((f"-" * 30) +
                  f"\nVocê jogou {jogador} e o computador {computador}. Total deu {soma} DEU IMPAR\n" +
                  ("-" * 30))
            print("Você VENCEU!\nVamos jogar novamente...\n" +
                  ("=-" * 15))
            vitoriasConsecutivas += 1

print(f"GAME OVER! Você venceu {vitoriasConsecutivas} vezes.")