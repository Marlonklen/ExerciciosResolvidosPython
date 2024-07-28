"""ESCREVA UM PROGRAMA QUE LEIA UJM SALÁRIO DEN UM FUNCIONÁRIO E CAUCULE O VALOR DO SEU AUMENTO.
PARA SALÁRIOS SUPERIORES A 1.250,00 CAUCULE UM AUMENTO DE 10%
PARA SALARIOS INFERIORES OU IGUAIS CAUCULE UM AUMENTO DE 15%."""
salario = float(input('Digite aqui o valor do salário do funcionário: '))
superior = 1.250
if salario > superior:
    print('O novo salário do funcionário será: {}'.format((salario * 10 / 100) + salario))

else:
    print('O novo salário do funcionário será: {}'.format((salario * 15 / 100) + salario))
