# O mesmo professor do desfio 19 quer sortear a ordem de apresentação do trabalho dos alunos. Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem certa.
import random

n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a ordem para apresentação do trabalho sera:')
print (lista)