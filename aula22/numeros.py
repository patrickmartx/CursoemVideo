# Módulos e Pacotes
'''
Podemos criar no python um pacote separado por vários assuntos para não sobrecarregar o programa.
import uteis
ou
from uteis import datas (o que seriam todas as funçoes voltadas pra datas)
from uteis import cores
'''

from uteis import numeros

num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {numeros.dobro(num)}")