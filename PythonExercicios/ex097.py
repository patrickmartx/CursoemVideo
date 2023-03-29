# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parãmetro e mostre uma mensagem com tamanho adaptável.
def escrevaTexto(txt):
    tam = len(txt) + 4
    print("~" * (tam))
    print(f"{txt:^{(tam)}}")
    print("~" * (tam))


escrevaTexto("Patrick Martins")
escrevaTexto("Curso de Python no YouTube")
escrevaTexto("CeV")