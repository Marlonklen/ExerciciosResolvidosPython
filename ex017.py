from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('a medida da hipotenuza é {:.2f}'.format(hi))


'''co = float(input('Digite o valor de cateto oposto: '))
ca = float(input('Digite o valor de cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenuza é {:.2f}. '.format(hi))'''