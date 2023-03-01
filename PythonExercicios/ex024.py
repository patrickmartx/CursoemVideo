# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input("Escreva o nome de uma cidade: ").strip()
'''
print(f"A cidade {cidade.title()} ", end="")
cidade = cidade.split(' ')

if cidade[0].lower() == "santo":
    print("começa com Santo!")
else:
    print("não começa com Santo!")
'''
print(cidade[:5].lower() == 'santo')