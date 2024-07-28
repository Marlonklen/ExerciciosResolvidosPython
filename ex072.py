'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem
por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.'''

extenso = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE',
         'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESEIS', 'DEZESETE',
         'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    numero = int(input('Digite um numero de 0 á 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('tente novamente!!Digite um numero de 0 á 20:'))
    print(f'Você digitou {extenso[numero]}')
    resp = str(input('Deseja continuar? S/N:')).strip().upper()
    if resp in 'nN':
        break
print('Obrigado por participar!')



