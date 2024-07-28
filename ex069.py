'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

print('~'*20)
print('  CADASTRAMENTO')
print('~'*20)
idademais18 = 0
homen = 0
mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()[0]
    while not sexo in 'FM':
        sexo =str(input('Digite o sexo: [M/F]')).upper().strip()[0]
    print('-'*20)
    print('USUÁRIO CADASTRADO')
    print('-'*20)
    if idade > 18:
        idademais18 += 1
    if sexo in 'M':
        homen += 1
    if sexo in 'F' and idade < 20:
        mulheres += 1
    resp = str(input('\033[1;33mDeseja continuar: [S/N]\033[m ')).upper().strip()[0]
    while not resp in 'NS':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
      break
print(f'Dentre as pessoas cadastradas, {idademais18} tem mais de 18 anos!')
print(f'{homen} homens foram cadastrados, {mulheres} mulheres tem menos de 20 anos. ')

