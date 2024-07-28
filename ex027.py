# Faça um progrma que leia um nome completo e mostre seu promeiro e ultimo nome separadamente:
nome = str(input('Digite seu nome completo: ')).title().split()
primeiro = nome[0]
ultimo = len(nome[-1])
print('PRIMEIRO NOME: {}'.format(primeiro))
print('ULTIMO NOME: {}'.format(ultimo))
