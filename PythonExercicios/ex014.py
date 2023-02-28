# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Digite a temperatura em celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"A temperatura em {celsius:.1f}ºC corresponde a {fahrenheit:.1f}ºF.")