# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parãmetro e mostre uma mensagem com tamanho adaptável.
def escrevaTexto(txt):
    tam = len(txt)
    print("~" * (tam + 4))
    print(f"{txt:^{(tam + 4)}}")
    print("~" * (tam + 4))


escrevaTexto("Patrick Martins")
escrevaTexto("Curso de Python no YouTube")
escrevaTexto("CeV")