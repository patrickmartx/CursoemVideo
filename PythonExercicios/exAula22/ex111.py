# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from PythonExercicios.exAula22.utilidadesCeV import moeda

p = float(input("Digite o preço: R$"))
print(f"A medade de {moeda.moeda(p)} é {moeda.metade(p, True)}.")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.")
print(f"Aumentando 10%, temos {moeda.aumentar(p, 10, True)}.")
print(f"Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}.")
moeda.resumo(p, 80, 35)
