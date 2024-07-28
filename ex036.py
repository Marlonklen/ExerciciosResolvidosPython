"""ESCREVA UM PROGRAMA QUE APROVE UM EMPRESTIMO BANCÁRIO PARA COMPRA DE UMA CASA.
O PROGRMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E QUANTOS ANOS ELE PRETENDE PAGAR.
 CAUCULE O VALOR DA PRESTAÇÃO, SABENDO QUE ELA NÃO PODE ESCEDER 30% DO SALÁRIO DO COMPRADOR OU ENTÃO
 O EMPRÉSTIMO NÃO SERÁ APROVADO!"""
valor = float(input('Qual o valor do imóvel: '))
salario = float(input('Qual é o salário base do usuário: '))
anos = int(input('Em quantos anos pretende pagar: '))
mensal = (valor // anos) // 12
if (salario * 30 // 100) >= mensal:
    print('O valor da sua prestação mensal do imóvel será de {:.2f}'.format(mensal))
else:
    print('Seu empréstimo foi negado, caucule novamente com maior quantidade de anos!')