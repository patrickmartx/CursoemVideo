# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

alunoA = input("Primeiro aluno(a): ")
alunoB = input("Segundo aluno(a): ")
alunoC = input("Terceiro aluno(a): ")
alunoD = input("Quarto aluno(a): ")
listaAlunos = [alunoA, alunoB, alunoC, alunoD]
random.shuffle(listaAlunos)

print("A ordem de apresentação será:")
print(listaAlunos)