"""Faça um programa que tenha uma função chamada área(), que receba as dimensões
 de um terreno retangular (largura e comprimento) e mostre a área do terreno."""

def área(larg, comp):
    a = larg * comp
    print(f'A áerea de um terreno {larg} x{comp} é de {a}M2.')

print('-='*20)
print('Controle de Terrenos')
print('-='*20)
l = float(input('LARGURA do terreno em M2. '))
c = float(input('COMPRIMENTO do terreno em M2. '))
área(l, c)
