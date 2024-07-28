n1 = int(input('\033[7;40mdigite um valor:\033[m '))
n2 = int(input('\033[7;40mdigite um outro valor:\033[m '))
s = n1 + n2
print('a soma entre \033[33;40m{}\033[m e \033[33;40m{}\033[m vale \033[30;43m{}\033[m'.format(n1, n2, s))

