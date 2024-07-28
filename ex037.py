"""ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E PEÇA O
USUÁRIO PARA ESCOLHER A BASE CONVERSÃ0:
1 PARA BINÁRIO
2 PARA OCTAL
3 PARA HEXADECIMAL"""
n = int(input('Digite um numero qualquer:'))
print("""Transformando numero decimal em outra base numérica:
(1) Decimal em binario
(2) Decimal para octal
(3) Decimal para Hexadecimal""")
r = int(input('Sua opção:'))
if r == 1:
    print('O Numero dicimal {} em binário é {}'.format(n, bin(n)[2:]))

elif r == 2:
    print('O Numero decimal {} em octal é {}'.format(n, oct(n)[2:]))
elif r == 3:
    print('O numero dicimal {} em Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Você digitou uma opção invalida!')






