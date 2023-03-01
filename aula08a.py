# Utilizando módulos
import math, random

'''
biblioteca math {
ceil = arredondar pra cima
floor = arredondar pra baixo
trunc = retira ou organiza o número de casas pós vírgula.
pow = potenciação
sqrt = raiz quadrada
factorial = fatorial
}
'''
num = random.randint(1, 120)
raiz = math.sqrt(num)
print("A raiz de {} é igual a {}.".format(num, math.trunc(raiz)))




