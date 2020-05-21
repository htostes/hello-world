i1 = float(input('Digite um numero: '))
i2 = float(input('Digite outro numero: '))
i3 = float(input('Digite o ultimo numero: '))
if i1 > i2 and i1 > i3:
    maior = i1
else:
    if i2 > i3:
        maior = i2
    else:
        maior = i3
if i1 < i2 and i1 < i3:
    menor = i1
else:
    if i2 < i3:
        menor = i2
    else:
        menor = i3
print('O maior valor é {}\n'
      'O menor valor é {}'.format(maior, menor))
