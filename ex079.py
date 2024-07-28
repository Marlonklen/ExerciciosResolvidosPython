'''Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

cadastro = []
while True:
    num = int(input('Digite um numero:'))
    if num not in cadastro:
        print('-=' * 30)
        print(f'numero {num} cadastrado!')
        print('-=' * 30)
        cadastro.append(num)
    else:
        print('-=' * 30)
        print(f'Numero {num} não cadastrado, pois já existe em lista')
        print('-=' * 30)

    resp = str(input('Deseja continuar? S/N '))
    if resp in 'Nn':
        break

print('-='*30)
cadastro.sort()
print(f'Você cadastros os valores {cadastro}')
