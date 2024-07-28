'''Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''

print('-'* 30)
print(' '*2, 'SEQUÊNCIA DE FIBONACCI')
print('-'*30)
numero = int(input('Quantos termos deseja mostrar? '))
print('~'*30)
t1 = 0
t2 = 1
print('{} » {} » '.format(t1,t2), end='')
count = 3
while count <= numero:
    t3 = t1 + t2
    print('{} » '.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print('Fim')
print('~'*30)
