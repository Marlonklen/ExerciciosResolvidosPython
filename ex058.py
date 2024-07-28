'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''


from random import randint
from time import sleep
from emoji import emojize
numc = randint(0,10)
numj = 11
quantjogada = 0
print('-'* 5,'Vamos jogar??', '-' * 5,)
print('-'* 4, 'Vou pensar em um numero', '-' * 4)
print('º', end='')
sleep(1)
print('º', end='')
sleep(1)
print(emojize('º\U0001f914', use_aliases=True))
while numc != numj:
    numj = int(input('Qual numero acha que pensei? '))
    quantjogada += 1
    if numj == numc:
        print('Você acertou parabéns!!')
    elif numj < numc:
        print('Mais... Tente novamente!')
    elif numj > numc:
        print('Menos... Tente novamente!')
print('O numero pensado por mim foi {} e o numero digitado por você fou {}.'.format(numc, numj))
print('Você tentou acertar {} vezes.'.format(quantjogada))

