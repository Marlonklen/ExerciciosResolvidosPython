'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posições na lista.'''

lista = list()
maior = 0
menor = 0
for pos in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {pos}: ')))
    if pos == 0:
        maior = menor = lista[pos]
    else:
        if lista[pos] > maior:
            maior = lista[pos]
        if lista[pos] < menor:
            menor = lista[pos]

print('-='*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')

print(f'\nO Menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print('-='*30)

