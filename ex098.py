""" Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através
 da função criada:
 a) de 1 até 10, de 1 em 1
 b) de 10 até 0, de 2 em 2
 c) uma contagem personalizada"""
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='* 20)
    print(f'Contagem de {i} até {f} pulando de {p} em {p}')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='* 20)
print('Agora é sua vez de personalizar...')
ini = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PULO: '))
contador(ini, fim, passo)