# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input("Digite um ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"No ângulo {angulo}º, temos:\nSeno: {seno:.2f}\nConsseno: {cosseno:.2f}\nTangente: {tangente:.2f}")