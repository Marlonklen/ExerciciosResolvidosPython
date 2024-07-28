nome = str(input('digite o nome do aluno: '))
n1 = float(input('digite a preimeira nota:'))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))
m = n1 + n2 + n3
print('A média das notas de {} é {:.3f}'.format(nome, m / 3))
