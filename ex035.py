"""DESENVOLVA UM PROGRAMA QUE LEIAO COMPRIMENTO TRES RETAS DE UM E DIGA
 SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO."""
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('os numeros podem fomar um triangulo.')
else:
    print('Os numeros não formam um triangulo.')