'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:'''

frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('Na frase {} temos o inverso {}\n Portanto temos um Palindromo'.format(junto, inverso))
else:
    print('Na frase {} temos o inverso {}\n Portanto não temos um Palindromo'.format(junto, inverso))
