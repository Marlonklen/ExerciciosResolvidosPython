'''Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''

Num = [[],[]]

for c in range(1,8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        Num[0].append(valor)
    else:
        Num[1].append(valor)
Num[0].sort()
Num[1].sort()
print("-=" * 30)
print(f"Os números pares digitados foram {Num[0]}.")
print(f"Os números ímpares digitados foram {Num[1]}.")

