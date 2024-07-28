'''from math import factorial
n = int(input('Digite um  numero e veja seu fatorial!:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''


'''n = int(input('Digite um numero e veja seu fatorial: '))
c = n
f = 1
print('Cauculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

n = int(input('Digite um numero e veja seu fatorial: '))
f = 1
print('Cauculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))






