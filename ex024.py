# Crie um progrma que leia o nome de uma cidade e diga se ela inicia ou não com palavra santo.
cidade = str(input('Digite o nome de sua cidade: '))
posicao = cidade.find('Santo')
if posicao == 0:
    print('Sua cidade começa com Santo')
else:
    print('sua cidade não começa com Santo')

'''cid = str(input('Digite a sua cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')