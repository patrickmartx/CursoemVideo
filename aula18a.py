# LISTAS parte 2

'''teste = list()
teste.append('Patrick')
teste.append('23')
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''pessoas = [['Pedro', 1], ['Tiago', 2], ['João', 3], ['Barquinho', 4]]
print(pessoas[0][0])
for p in pessoas:
    print(f"{p[0]} é o {p[1]}º na música")'''

galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmen += 1

print(f"Temos {totmai} maiores de idade e {totmen} menores de idade.")