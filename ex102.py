"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor
 lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo
 do fatorial."""
def fatorial(n, Show=False):
    """
    -> Caucula o fatorial de um número
    :param n: O número a ser cauculado.
    :param Show: mostrar ou não ou cáuculo fatorial.
    :return: O valor fatorial de um número.
    """
    f = 1
    for c in range(n, 0, -1):
        if Show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa principal
print(fatorial(5, Show=True))
help(fatorial)