"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
 cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
 além da idade, com quantos anos a pessoa vai se aposentar."""
from datetime import  datetime
dados = dict()
dados['Nome'] = str(input('Digite o nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['cpts'] = int(input('Carteira de trabalho: (0 não tem)'))
if dados['cpts'] != 0:
    dados['contratação'] = int(input('Ano da contratação: '))
    dados['salário'] = float(input('Salário Atual: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='* 30)
for k, v in dados.items():
    print(f'{k} = {v}')
