# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados | B) Os últimos 4 colocados na tabela. | C) Uma lista com os times em ordem alfabética. | D) Em que posição na tabela está o time Bragantino.

tabelaBrasileirao2022 = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico Paranaense', 'Atlético Mineiro', 'Fortaleza', 'São Paulo', 'América Fc', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético', 'Avaí', 'Juventude')

print("-="*20)
print("Lista de times do Brasileirão: (", end=' ')
for times in range(0, len(tabelaBrasileirao2022)):
    if tabelaBrasileirao2022[times] != tabelaBrasileirao2022[-1]:
        print(f"{tabelaBrasileirao2022[times]},", end=" ")
    else:
        print(f'{tabelaBrasileirao2022[times]} )')
print("-="*20)

print(f"Os 5 primeiros colocados sâo: {tabelaBrasileirao2022[0:5:1]}")

print("-="*20)

print(f"Os 4 últimos colocados sâo: {tabelaBrasileirao2022[len(tabelaBrasileirao2022) - 4:len(tabelaBrasileirao2022): 1]}")

print("-="*20)

print(f"Times em ordem alfabética: {sorted(tabelaBrasileirao2022)}")

print("-="*20)

for time in range(0, len(tabelaBrasileirao2022)):
    if tabelaBrasileirao2022[time] == 'Bragantino':
        print(f"O {tabelaBrasileirao2022[time]} está em {time+1}º lugar.")