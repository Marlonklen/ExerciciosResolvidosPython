"""CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR"""
num = int(input('Digite um numero: '))
if (num % 2) == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é IMPAR.'.format(num))

