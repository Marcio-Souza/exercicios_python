"""
    Sorteio de alunos.
    Recebe os inputs de nomes de alunos e faz um sorteio
    Ex. 
    >>>Digite o nome do Aluno: João
    >>>Digite o nome do Aluno: Maria
    >>>Digite o nome do Aluno: Antônio
    >>>Digite o nome do Aluno: Pedro
    >>>Aluno sorteado: Antônio

"""
from random import randint

alunos = []

for n in range(0,4):
    alunos.append(input("Digite o nome do aluno: "))

sorteio = randint(0,4)

print(f'Aluno sorteado: {alunos[sorteio]}')
