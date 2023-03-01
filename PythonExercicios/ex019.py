# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice

alunoA = input("Primeiro aluno(a): ")
alunoB = input("Segundo aluno(a): ")
alunoC = input("Terceiro aluno(a): ")
alunoD = input("Quarto aluno(a): ")
listaAlunos = [alunoA, alunoB, alunoC, alunoD]

print(f"O aluno(a) escolhido(a) foi {choice(listaAlunos)}")