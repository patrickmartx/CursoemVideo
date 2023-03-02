# Condições (Parte 1)
class avaliacao:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    media = (n1 + n2) / 2


print(f"A sua média foi: {avaliacao.media}")
if avaliacao.media >= 6.0:
    print("Você passou!")
else:
    print("Você reprovou!")
