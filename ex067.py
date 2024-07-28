'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
n = 0
count = 0
while True:
    print('-»' * 20)
    n = int(input('Digite um numero para ver sua tabuada: '))
    print('-»'*20)
    if n < (n-n):
        break
    while count <= 10:
        print(f'{n} X {count} = {n * count}')
        count += 1
    count = 0
print('Programa tabuada encerrado! Volte sempre!')
