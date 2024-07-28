"""Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
nome = str(input('Qual é eu seu nome: '))
print('Olá {}!'.format(nome))
sexo = int(input("""Qual o seu sexo:
 [ 1 ] FEMININO 
 [ 2 ] MASCULINO\n"""))
if sexo == 1:
    print('Segundo a lei de alistamento por ser do sexo feminino você não precisa se alistar!')
elif sexo == 2:
    ano = int(input('Digite o ano do seu nascimento:'))
    idade = date.today().year - ano
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, date.today().year))
    if idade < 18:
        print('Você ainda deve se alistar! Faltam {} ano para o alistamento procure a junta neste período!'.format(18 - idade))
    elif idade == 18:
        res = int("""Você já se alistou?
         [ 1 ] SIM
         [ 2 ] NÃO\n""")
        if res == 1:
            print('Parabéns você cumpriu com os deveres de um cidadão.')
        elif res == 2:
            print('Você esta na idade de se alistar! proucure a Junta mais proxima!')
        else:
            print('Você digitou a opção inválida, digite novamente.')
    else:
        res = int(input("""Você ja se alistou:
        [ 1 ] SIM
        [ 2 ] NÃO\n"""))
        if res == 1:
            print('Parabéns você cumpriu com os deveres de um cidadão.')
        elif res == 2:
            print('Você passou {} anos da idade para se alistar, proucure a Junta e regularize sua situação!'.format(idade - 18))
        else:
            print('Você digitou a opção inválida, digite novamente.')
else:
    print('OPÇÃO INVALIDA! DIGITE NOVAMENTE')

