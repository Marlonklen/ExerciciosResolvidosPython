# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que deseja: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo digitado {}, tem o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'.format(ângulo, seno, cosseno, tangente))
