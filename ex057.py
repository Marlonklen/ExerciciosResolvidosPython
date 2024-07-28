'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Você digitou sexo invalido, digite seu sexo: [M/F] ')).upper().strip()[0]

print('sexo {} cadastrado com sucesso.'.format(sexo))
