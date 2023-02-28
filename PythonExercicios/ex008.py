# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input("Digite um valor em metros: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f"Valor digitado: {m}")
print(f"Valor Quilômetros: {km}")
print(f"Valor Hectômetros: {hm}")
print(f"Valor Decâmetros: {dam}")
print(f"Valor Decimetros: {dm}")
print(f"Valor Centimetros: {cm}")
print(f"Valor Milimetros: {mm}")