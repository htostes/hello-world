# Ler vários valores e colocar em uma lista
numeros = list()
while True:
    print('-'*30)
    num = int(input('Digite um valor: '))
    if num in numeros:
        print('Valor duplicado. Não foi adicionado.')
    else:
        numeros.append(num)
        print('Valor adicionado com sucesso.')
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if c == 'N':
        break
numeros.sort()
print('-'*30)
print(f'Lista final: {numeros}')
