# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas
# > O nome com todas minúsculas
# > Quantas letras ao total (sem considerar espaços)
# > quantas letras tem o primeiro nome

nomeCompleto = input("Escreva o seu nome completo: ").strip()
print(f"Nome com todas as letras maiúsculas: {nomeCompleto.upper()}")
print(f"Nome com todas as letras minúsculas: {nomeCompleto.lower()}")
print(f"Quantidade de letras sem contar os espaços: {len(nomeCompleto)-nomeCompleto.count(' ')}")
nomeSeparado = nomeCompleto.split(' ')
print(f"Quantiadade de letras no primeiro nome: {len(nomeSeparado[0])}")
