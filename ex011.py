a = float(input('digite a altura da parede: '))
l = float(input('digite o valor da largura da parede: '))
m = a * l
print('sua parede tem a dimensão de: {}x{} e sua área tem {:.4f}M2'.format(a, l, m))
print('para pintar essa parede você precisará de {:.4f}l de tinta'.format(m / 2))


