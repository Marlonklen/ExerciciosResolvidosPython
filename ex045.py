"""Crie um programa que faça o computador jogar Jokenpô com você."""
from random import randint
from time import sleep
print('''\033[2;36mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
jogador = int(input('\033[1mQual é sua jogada?\n\033[m'))
computador = randint(0, 2)

if computador == 0:
    computador = 'PEDRA'
elif computador == 1:
    computador = 'PAPEL'
elif computador == 2:
    computador = 'TESOURA'
if jogador == 0:
    jogador = 'PEDRA'
elif jogador == 1:
    jogador = 'PAPEL'
elif jogador == 2:
    jogador = 'TESOURA'
else:
    print('\033[0;31mVocê digitou a opção errada tente novamente!\033[m')
    quit()
print('\033[1;31mJÔÔ\033[m')
sleep(1)
print('\033[1;32mKEN\033[m')
sleep(1)
print('\033[1;34mPôÔ\033[m')
sleep(1)
print(15 * '\033[0;33m-=\033[m')
print('O computador jogou \033[1;31m{}\033[m'.format(computador))
print('O Jogador jogou \033[1;31m{}\033[m'. format(jogador))
print(15 * '\033[0;33m-=\033[m')
if computador == 'PEDRA' and jogador == 'PAPEL':
    print('\033[1;33mJOGADOR VENCE!\033[m')
elif computador == 'PAPEL' and jogador == 'TESOURA':
    print('\033[1;33mJOGADOR VENCE!\033[m')
elif computador == 'TESOURA' and jogador == 'PEDRA':
    print('\033[1;33mJOGADOR VENCE!\033[m')
elif computador == 'PEDRA' and jogador == 'TESOURA':
    print('\033[1;33mCOMPUTADOR VENCE!\033[m')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print('\033[1;33mCOMPUTADOR VENCE!\033[m')
elif computador == 'TESOURA' and jogador == 'PAPEL':
    print('\033[1;33mCOMPUTADOR VENCE!\033[m')
else:
    print('\033[33;47mAMBOS SÃO IGUAIS, DEU EMPATE!\033[m')
