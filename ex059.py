'''Crie um programa que leia dois valores e mostre um menu na tela:'''
valor1 = int(input('digite um valor: '))
valor2 = int(input('Digite outro valor: '))
sair = 0
valormaior = 0
while sair != 5:
    resp = int(input('[ 1 ] SOMAR\n[ 2 ]MULTIPLICAR\n[ 3 ]MAIOR\n[ 4 ]NOVOS NUMEROS\n[ 5 ]SAIR DO PROGRAMA\n'))
    if resp == 1:
        print('O resultado da soma de {} com {} é de {}.\n'.format(valor1, valor2, valor1 + valor2))
    if resp == 2:
        print('O resultado da multiplicação de {} por {} é {}.\n'.format(valor1, valor2, valor1 * valor2))
    if resp == 3:
        valormaior = valor1
        if valor2 > valormaior:
            valormaior = valor2
            print('O valor maior digitado é {}.\n'.format(valormaior))
    if resp == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro Valor:'))
    if resp == 5:
        sair = 5
print('Agradeço seu engajamento conosco! até a proxima!')
