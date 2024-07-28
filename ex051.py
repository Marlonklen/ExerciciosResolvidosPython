'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 No final, mostre os 10 primeiros termos dessa progressão'''
primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
prog = primeiro + (10 ) * razao
for c in range(primeiro, prog, razao):
    print('{}'.format(c), end=' >> ')
print('ACABOU')

