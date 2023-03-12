# Refaça o desafio 35 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais | Isósceles: dois lados iguais | Escaleno: Todos os lados diferentes.

retaA = float(input("Digite o valor da reta A: "))
retaB = float(input("Digite o valor da reta B: "))
retaC = float(input("Digite o valor da reta C: "))

if retaA < retaB + retaC and retaB < retaA + retaC and retaC < retaA + retaB:
    print("É possível formar um triângulo.")
    '''if (retaA == retaB) and (retaB == retaC):
        print("É um triângulo equilátero.")
    elif ((retaA == retaB) and (retaA != retaC)) or ((retaB == retaC) and (retaB != retaA)) or ((retaC == retaA) and retaC != retaB):
        print("É um triângulo Isósceles.")
    elif ((retaA != retaB) and (retaA != retaC)) or ((retaB != retaC) and (retaB != retaA)) or ((retaC != retaA) and retaC != retaB):
        print("É um triângulo Escaleno.")'''
    if retaA == retaB == retaC:
        print("É um triângulo equilátero.")
    elif retaA != retaB != retaC != retaA:
        print("É um triângulo Escaleno.")
    else:
        print("É um triângulo Isósceles.")
else:
    print("Não é possível formar um triângulo.")

