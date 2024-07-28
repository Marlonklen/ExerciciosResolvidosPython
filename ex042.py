"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('os numeros podem fomar um triangulo.')
    if r1 == r2 and r2 == r3:
        print('O triangulo formado é um triangulo EQUILÁTERO')
    if r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo formado é um triângulo ISÓSCELES')
    if r1 != r2 and r2 != r3 and r3 != r1:
        print('O triângulo formado é um triângulo ESCALENO')

else:
    print('Os numeros não formam um triangulo.')


