"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""
print('{:-^40}'.format(' Marlon store '))
preco = float(input('Valor do produto:\n '))
opcao = int(input("""FORMA DE PAGAMENTO:
 [ 1 ] À VISTA DINHEIRO / CHEQUE
 [ 2 ] À VISTA NO CARTÃO
 [ 3 ] EM ATÉ 2 VEZES NO CARTÃO
 [ 4 ] 3 VEZES NO CARTÃO \n """))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao== 4:
   total = preco + (preco * 20 / 100)
   parctotal = int(input('quantas parcelas:\n'))
   parcela = total / parctotal
   print('sua compra será parcelada em {}x de R${:.2f}'.format(parctotal, parcela))
else:
    total = preco
    print('Opção Invalida de pagamento')
print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(preco, total))
