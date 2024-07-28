'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
vitorias = valor = valorpc = 0
par = impar = escolhausu = ''

print('-=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR!')
print('-=-'*  20)

while True:
    valorpc = randint(0,10)
    valor = int(input('Digite um valor inteiro positivo: '))
    escolhausu = str(input('Você quer PAR ou IMPAR? [P/I]')).upper().strip()[0]
    print('-'*20)
    if (valor + valorpc) % 2 == 0:
        print(f'Você jogou {valor} e o computador jogou {valorpc}. o total deu {valor + valorpc} é PAR')
    else:
        print(f'Você jogou {valor} e o computador jogou {valorpc}. O total {valor + valorpc} é IMPAR')
    print('-'* 20)
    if (valor + valorpc) % 2 == 0 and escolhausu in 'P':
        vitorias += 1
        print('Você venceu!!\n Vamos Jogar novamente...')
    elif (valor + valorpc) % 2 != 0 and escolhausu in 'I':
        vitorias += 1
        print('Você venceu!!\nVamos Jogar novamente...')
    else:
        print('você perdeu!')
        break
print(f'Game Over! Você venceu {vitorias} vezes.')
