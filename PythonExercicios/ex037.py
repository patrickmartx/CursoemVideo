# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
# 1 para binário | 2 para octal | 3 para hexadecimal

def interface():
    print("\nPROGRAMA DE CONVERSÃO\nEscolha uma opção que indique como você quer que seu numero interiro seja retornado:")
    opcao = int(input("1 - Binário\n2 - Octal\n3 - Hexadecimal\nEscreva sua opção: "))
    if (opcao >= 1) and (opcao <= 3):
        return opcao
    else:
        print("OPÇÃO INVÁLIDA!")
        return  interface()

def conversao(nInt, op):
    if op == 1:
        return print(format(nInt, 'b'))
    elif op == 2:
        return print(format(nInt, 'o'))
    elif op == 3:
        return print(format(nInt, 'x'))

numeroInteiro = int(input("Digite um número inteiro: "))
opcao = interface()
numeroConvertido = conversao(numeroInteiro, opcao)