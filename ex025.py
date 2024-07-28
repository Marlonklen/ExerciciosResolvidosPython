# Crie um programa que leia o nome de uma pessoa e diga se ela tem ou não Silva no nome.
nome = str(input('Digite seu nome: ')).title()
print('Seu nome tem silva: {}'.format('Silva' in nome))
