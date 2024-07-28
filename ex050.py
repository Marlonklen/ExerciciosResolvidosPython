'''Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares.
 Se o valor digitado for ímpar, desconsidere-o.'''
s = 0
cont = 0
for c in range(1,7):
    numero = int(input('Digite um numero:'))
    if numero % 2 == 0:
        s += numero
        cont += 1

print ('Existem {} numeros pares, a somas dos numeros pares é: {}'.format(cont, s))

