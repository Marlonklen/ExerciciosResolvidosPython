'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão
 usando a estrutura while.'''
print('GERADOR DE PA!')
print('-='*10)
primeiroter = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiroter
count = 1

while count <= 10:
    print('{}'.format(decimo), end='')
    print(' » ' if count <= 10 else ' ', end='')
    decimo += razao
    count += 1
print('FIM')
