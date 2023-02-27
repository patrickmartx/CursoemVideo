# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input("Digite um valor em metros: "))
cm = m * 100
mm = m * 1000

print(f"Valor em metro: {m:.2f}\nConvertido em cm: {cm:.2f}\nConvertido em mm: {mm:.2f}")