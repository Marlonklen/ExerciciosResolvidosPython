from random import choice

# O professor de uma turma quer sortear 4 dos seu alunos para apagar o quadro, faça um programa que leia o nome dos 4
# e escolha um nome.

n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do proximo aluno: '))
n3 = str(input('Digite o nome do proximo aluno: '))
n4 = str(input('Digite o nome do proximo aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno sorteado é {}'.format(escolhido))

