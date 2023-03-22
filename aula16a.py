# Tuplas

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
'''for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')'''

# OU

'''for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")'''

# OU

'''for i in range(0, len(lanche)):
    if i == 0:
        print(f'Eu vou comer {i}º: {lanche[i]}')
    else:
        print(f"e também {i}º: {lanche[i]}")
print('Comi pra caramba!')'''

'''print(sorted(lanche))'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c))
print(c.count(5))
print(c.index(8))
'''

pessoa = ('Patrick', 39, 'M', 80.1)
del(pessoa)
print(pessoa)