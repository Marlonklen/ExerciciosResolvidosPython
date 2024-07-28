'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

s = n = count = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    count += 1
print(f'Foram digitados {count} valores e a soma entre eles é {s}')
