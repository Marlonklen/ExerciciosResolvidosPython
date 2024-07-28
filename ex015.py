km = float(input('Informe o quilômetro percorrido: '))
dias = int(input('informe a quantidade de dias alugados: '))
valor_km = km * 0.15
valor_dia = dias * 60
total = valor_dia + valor_km
print('O valor correpondente a quantidade de km é {}R$, e a quantidade de dias é {:.2f}R$, o valor total a pagar é {:.2f}R$.'.format(valor_km, valor_dia, total))
