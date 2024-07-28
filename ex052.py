'''Faça um programa que leia um número inteiro e diga

se ele é ou não um número primo.'''
numero = int(input('Digite um numero:'))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[31m', end='')
        tot += 1
    else:
        print('\033[0m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número \033[1;31m{}\033[m foi dividido \033[1;31m{}\033[m vezes'.format(numero, tot))
if tot == 2:
    print('O numero \033[1;31m{}\033[m é um numero PRIMO!'.format(numero))
else:
    print('O número \033[1;31m{}\033[m NÃO É um numero PRIMO!'.format(numero))




