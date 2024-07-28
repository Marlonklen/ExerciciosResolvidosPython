algo = input('\033[4;35mdigite algo:\033[m')
print('\033[35mO tipo primitivo desse valor é:\033[m', type(algo))
print('\033[1;30;47mSó tem espaços?\033[m ', algo.isspace())
print('\033[4;31;46mÉ numero?\033[m', algo.isnumeric())
print('\033[7;32;45mÉ alfabético?\033[m', algo.isalpha())
print('\033[0;33;44mÉ alfanumérico?\033[m', algo.isalnum())
print('\033[1;34;43mÉ maiúscula?\033[m', algo.isupper())
print('\033[4;35;42m minúscula?\033[m', algo.islower())
print('\033[7;36;41mesta capitalizada?', algo.istitle(),'\033[m')


