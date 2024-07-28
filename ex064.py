'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
 foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

soma = count = 0
numeros = int(input('Digite um numero: '))
while numeros != 999:
    soma += numeros
    count +=1
    numeros = int(input('Digite um numero: '))
print('Foram digitados {} numeros e a soma deles é {}'.format(count, soma))
