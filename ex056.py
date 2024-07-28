'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaidade = 0
idademaisvelho = 0
homemaisvelho = ''
mulhermenor20 = 0
for p in range(1,5):
    print('-'*10,'{}ª PESSOA'.format(p),'-'*10,)
    nome = str(input('nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        idademaisvelho = idade
        homemaisvelho = nome
    if sexo in 'M' and idade > idademaisvelho:
        idademaisvelho = idade
        homemaisvelho = nome
    if sexo in 'F' and idade < 20:
        mulhermenor20 += 1

print('A média das idades digitadas é {}.'.format(somaidade / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(idademaisvelho, homemaisvelho))
print('Nas pessoas digitadas acima {} mulheres te menos de 20 anos'.format(mulhermenor20))
