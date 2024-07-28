'''Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:'''

times =('ATLÉTICO MG', 'PALMEIRAS', 'FLAMENGO', 'FORTALEZA',
       'RED BULL BRAGANTINO', 'CORINTHIANS', 'INTERNACIONAL',
       'FLUMINESE', 'CUIABÁ','ATLÉTHICO PR', 'ATLÉTICO GO',
       'SÃO PAULO', 'CEARÁ', 'SANTOS', 'BAHIA', 'AMÉRICA MG',
       'JUVENTUDE', 'GRÉMIO', 'SPORT', 'CHAPECOENSE')
print(f'Os 5 primeiros colocados são:{times[0:5]} ')
print(f'Os 4 últimos colocados são:{times[-4:]}')
print(sorted(times))
print(f'O time CHAPECOENSE está na {times.index("CHAPECOENSE")+1}ª posição')

