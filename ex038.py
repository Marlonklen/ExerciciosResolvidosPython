num1 = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero:'))
if num1 > num2:
    print('O numero {} é maior que o numero {}'.format(num1, num2))
elif num1 < num2:
    print('O numero {} é menor que o numero {}'.format(num1, num2))
else:
    print('Ambos os valores são iguais')
