"""Faça um programa que leia o nome e média de um aluno guardando tambem
em um dicionário no final mostre o conteúdo da estrutura na tela."""

aluno = {}
situacao = {}
aluno['Nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['media'] >= 7.0:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] <= 3.0:
    aluno['situacao'] = 'reprovado'
elif aluno['media'] < 7.0 and aluno['media'] > 3.0:
    aluno['situacao'] = 'Recuperação'

print('-=' * 20)
for k, v in aluno.items():
  print(f'{k} é igual a {v}')
