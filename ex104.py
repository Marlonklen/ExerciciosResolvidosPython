"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante ‘a função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)"""
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite apenas um número inteiro válido!\033[m')
        if ok:
            break
    return valor


#Programa principal
n = leiaInt("Digite um numero inteiro: ")
print(f'Você acabou de digitar o número {n}.')