'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o
 menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
soma = count = maior = menor = 0
sair = ''
while sair != 'S':
    numero = int(input('Digite um valor: '))
    soma += numero
    count += 1
    if count == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    sair = str(input('Deseja sair? S/N ')).strip().upper()[0]
media = soma / count
print('A media dos valores digitados é de {:.2f}, o maior valor é {} e o menor é {}.'.format(media, maior, menor))