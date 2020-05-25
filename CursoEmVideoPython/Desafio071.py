# Caixa eletronico
# Cédulas: 50, 20, 10, 1
fvalor = ivalor = int(input('Valor a ser sacado: R$'))
ced50 = ced20 = ced10 = ced1 = 0
while True:
    print('test  ')
    if fvalor // 50 > 0:
        ced50 = fvalor // 50
        fvalor -= ced50 * 50
    elif fvalor // 20 > 0:
        ced20 = fvalor // 20
        fvalor -= ced20 * 20
    elif fvalor // 10 > 0:
        ced10 = fvalor // 10
        fvalor -= ced10 * 10
    elif fvalor // 1 > 0:
        ced1 = fvalor // 1
        fvalor -= ced1 * 1
    if fvalor == 0:
        break
print(f'Saque:'
      f'\nCédulas de R$50: {ced50}'
      f'\nCédulas de R$20: {ced20}'
      f'\nCédulas de R$10: {ced10}'
      f'\nCédulas de R$1:  {ced1}'
      f'\nTotalizando: R${ivalor}')


