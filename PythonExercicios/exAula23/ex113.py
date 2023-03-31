# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
from utils import data

numInt = data.leiaInt("Digite um número inteiro: ")
numFloat = data.leiaFloat("Digite um número real: ")
data.imprimir(f"O valor inteiro digitado foi {numInt} e o valor real foi {numFloat}.", 2)