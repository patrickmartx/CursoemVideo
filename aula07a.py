# Operações Aritméticas

'''
+ = Adição | - = Subtração | * = Multiplicação | / = Divisão | ** = Potência | // = Divisão inteira | % = Resto da divisão
Ordem de precedência: 1 = () | 2 = ** | 3 = *,/,//,% | 4 = +, -
'''

'''nome = input("Qual o seu nome?: ")
print(f"Prazer em te conhecer, {nome:=^20}")'''

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.5f}.', end=' >>> ')
print(f'A divisão inteira é {di} e a potência {e}.')