# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
import emoji

print("FALTAM 10 SEGUNDOS PARA OS FOGOS!")
for i in range(10, -1, -1):
    sleep(1)
    print(i)
print(emoji.emojize(":sparkler::sparkler::sparkler::sparkler::sparkler::sparkler:"))
