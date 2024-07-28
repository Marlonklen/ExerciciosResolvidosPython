'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('-='*20)
print('BANCO MARLON KLEN')
print('-='*20)

valor = int(input('Qual Valor deseja sacar: '))
total = valor
cedula = 50
total_de_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_de_cedula += 1
    else:
        if total_de_cedula > 0:
            print(f'Total de {total_de_cedula} de R$ {cedula}')

        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_de_cedula = 0
        if total == 0:
            break
print('Progrmama finalizado!!')