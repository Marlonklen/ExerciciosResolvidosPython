"""A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""

from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano de nascimento do atleta: '))
idade = atual - nascimento
print('O atleta tem {} anos de idade.'.format(idade))
if idade <= 9:
    print('O atleta é da categoria MIRIM.')
elif idade > 9 and idade <= 14:
    print('O atleta é da categoria INFANTIL!')
elif idade > 14 and idade <= 19:
    print('O atleta é da categoria JUNIOR!')
elif idade > 19 and idade <= 25:
    print('O atleta é da categoria SÊNIOR!')
else:
    print('O atleta é da categoria MASTER!')