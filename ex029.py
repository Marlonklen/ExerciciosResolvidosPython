"""ESCREVA UM PROGRMA QUE A VELOCIDADE DE UM CARRO.
SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
A MULTA IRA CUSTAR 7,00R$ POR CADA KM ACIMA DO LIMITE."""
from random import randint
velocidade = randint(10, 120)
print('Você passou á {}km/h'.format(velocidade))
if velocidade > 80:
    multa = float(velocidade - 80)
    print('você ultrapassou a velocidade permitida! Você foi multado. Sua multa é de: {:.2f}R$'.format(multa * 7))
print('Boa viagem!')