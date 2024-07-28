#Faça um progrma que leia um numero digitado pelo usiario de 0 a 9999 e mostre na tela seus digitos
#  digitos separados.
numero = int(input('Digite um numero até 9999: '))
unidade = numero // 1 % 10
print('UNIDADE: {}'.format(unidade))
dezena = (numero) // 10 % 10
print('DEZENA: {}'.format(dezena))
centena = (numero) // 100 % 10
print('CENTENA: {}'.format(centena))
milhar = (numero) // 1000 % 10
print('MILHAR: {}'.format(milhar))
'''numero = int(input('Digite um numero:'))
num = str(numero)
print('Analizando o numero {}'.format(numero))
print('UNIDADE: {}'.format(num[3]))
print('DEZENA: {}'.format(num[2]))
print('CENTENA: {}'.format(num[1]))
print('MILHAR: {}'.format(num[0]))'''
