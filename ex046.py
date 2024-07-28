'''Faça um programa que mostre na tela uma contagem regressiva para o
estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep
import emoji
estouro = 10
final = 0
print('Os fogos de artificios estourarão em 10 segundos...')
sleep(2)
for c in range(estouro, final, -1):
    print(c)
    sleep(1)
print(emoji.emojize('\033[1;31mestourou :boom:', use_aliases=True))

