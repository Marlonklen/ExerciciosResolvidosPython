'''perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('GERADOR DE PA!')
print('-='*10)
primeiroter = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiroter
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print('{} » '.format(termo), end='')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos.'.format(total))

