from random import randrange

alunos = []

for n in range(4):
    alunos.append(input("Digite nome do Aluno: "))

sorteio = randrange(0, 4)
print(f'Aluno sorteado: {alunos[sorteio]}')
