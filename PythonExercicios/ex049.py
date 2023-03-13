# Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, ó que agora usando um laçõ FOR.

n = int(input("Digite um número: "))
print("="*10 + " TABUADA " + "="*10)
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
print("="*29)