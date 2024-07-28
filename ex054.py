'''Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
maioridade = 0
menoridade = 0
for c in range(1, 8, 1):
    ano = int(input('Digite o ano de nascimento da {} pessoa:'.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print('{} pessoas já atingiram a maior idade e {} ainda não atingiram a maior idade.'.format(maioridade, menoridade))



