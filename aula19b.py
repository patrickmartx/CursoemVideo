# DICIONÁRIOS

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).capitalize()
    estado['sigla'] = str(input('Sigla do estado: ')).upper()
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f"{v} ", end='')
    print()