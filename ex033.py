""" FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E MENOR"""
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
# verificando maior
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
print('O maior numero digitado é {}.'.format(maior))
# verificando menor
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print('O menor numero digitado é {}'.format(menor))
