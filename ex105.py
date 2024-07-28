"""Faça um programa que tenha uma função notas() que pode receber várias notas de
alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação """
def notas(*n, sit=False):
    """
    ->Função para analizar notas e situação de vários alunos.
    :param n: Uma ou mais notas de vários alunos.
    :param sit: Parâmetro opcional, indicando se deve ou não adicionar a situação da média de turma.
    :return: Um dicionário com as informações sobre as notas dos alunos.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r



#Programa principal

resp = notas(9.8, 8.7, 4.5, 7.0, sit=True)
print(resp)
help(notas)