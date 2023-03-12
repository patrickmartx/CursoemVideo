# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso | Entre 18.5 e 25: Peso ideal | 25 até 40: Sobrepeso | Acima de 40: Obesidade mórbita

altura = float(input("Digite a sua altura(em metros): "))
peso = float(input("Digite seu peso(em KG): "))

IMC = peso / (altura**2)

if (IMC < 18.5):
    print(f"Seu IMC é de {IMC:.2f} e você está abaixo do peso.")
elif (IMC >= 18.5)  and (IMC < 25):
    print(f"Seu IMC é de {IMC:.2f} e você está no peso ideal.")
elif (IMC >= 25) and (IMC < 40):
    print(f"Seu IMC é de {IMC:.2f} e você está com sobrepeso.")
else:
    print(f"Seu IMC é de {IMC:.2f} e você está com obesidade.")
