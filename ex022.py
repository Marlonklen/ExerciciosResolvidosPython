#Crie um programa que leia o nome completo de uma pessoa e mostre na tela:
# o nome com todas a letras maiuculas
# o nome com todas as letras minusculas
# Quantas letras tem sem considerar os espaços
# Quabtas letras tem o primeiro nome
nome = str(input('Digite um nome:')).strip()
maiuscula = nome.upper()
minuscula = nome.lower()
quantidade = len(''.join(nome.split()))
print(maiuscula)
print(minuscula)
print('o nome digitado contem {} caracteres.'.format(quantidade))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
