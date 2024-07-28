""" DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM QUILOMETRO
CAUCULE O PREÇO DA PASSAGEM R$0,50 POR KM E ACIMA DE 200KM R$0,45 PARA VIAGENS MAIS LONGAS.
"""
km = float(input('Digite o a quilometragem da viagem: '))
if km > 200:
    print('O valor da sua viagem correspondente á {}km será R${:.2f}'.format(km, km * 0.45))
else:
    print('O valor da sua viagem correspondente á {}km será R${:.2f}'.format(km, km * 0.50))

"""SIMPLIFICADO 
PRECO = DISTANCIA * 0.50 IF DISTANCIA <= 200 ELSE DISTANCIA * 0.45"""
