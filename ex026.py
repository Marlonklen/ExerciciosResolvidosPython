# Faça um progrma que leia uma frase digitada pelo usuário e mostre na tela:
# Quantas vezes aparece a letra A
# Em qual posição ela aprece a primeira vez
# Em qual posição elas aparece a ultima vez
frase = str(input('Digite uma frase: ')).strip()
frase = frase.lower()
quantidade = frase.count('a')
primeira = frase.find('a') + 1
ultima = frase.rfind('a') + 1
print('A leta A aprece {} vezes nessa frase.'.format(quantidade))
print('A letra A aprece na posição {} no inicio.'.format(primeira))
print('A letra A aprece na posição {} no final.'.format(ultima))
