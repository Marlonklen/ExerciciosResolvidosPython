soma = 0
mais_1000 = 0
mais_barato = ''
valor_barato = 0
resp = ''
count = 1
print('»«'*10)
print('REGISTRE SUA COMPRA')
print('»«'* 10)
while True:
    print('~'* 20)
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    valor = float(input('DIgite o valor do produto: '))
    print('~'*20)
    soma += valor
    if valor > 1000.00:
        mais_1000 += 1
    if count == 1:
        valor_barato = valor
        mais_barato = produto
    if valor < valor_barato:
        valor_barato = valor
        mais_barato = produto
    count += 1
    resp = str(input('\033[1;33mDeseja contunuar o registro? [S/N]\033[m ')).upper().strip()[0]
    while not resp in 'SN':
        resp = str(input('\033[1;34mDeseja contunuar o registro? [S/N]\033[m ')).upper().strip()[0]
    if resp in 'N':
        break

print('-'*20)
print(f'O total de gasto da sua compra é R$ {soma:.2f}')
print(f'Sua compra tem {mais_1000} produtos que vale mais de R$ 1.000.')
print(f'O artigo mais barato é o artigo : {mais_barato}.')
print('-'*20)
