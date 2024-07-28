"""FAÇA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSAR EM UM NUMERO DE 0 A 5 E PEÇA O USUÁRIO PARA
TENTAR DESCOBRIR QUYAL FOI O NUMERO PENSADO PELO COMPUTADOR. O PROGRMA DEVERÁ ECREVER NA TELA
SE O USUÁRIO PERDEU OU VENCEU."""
from random import randint
from time import sleep
num = randint(0, 5) #faz o computador "sortear".
print('-=-' *20)
print('Vou pensar em um número de 0 a 5!')
print('-=-' *20)
pensou = int(input('Qual numero acha que eu pensei? ')) # o usuario tenta adivinhar.
print('Processando...')
sleep(3)
if num == pensou:
    print('Você adivinhou o número, parabéns!!')
else:
    print('Você perdeu!! não foi dessa vez. Eu pensei no numero {} e não no {}'.format(num, pensou))


