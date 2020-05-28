numeros = list()
while True:
    numeros.append(int(input('Digite o número: ')))
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    print('-' * 30)
    if c == 'N':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} valores.')
print(f'A lista em ordem descrescente é {numeros}.')
if 5 in numeros:
    print(f'O número 5 está na lista e foi encontrado na {numeros.index(5) + 1}ª posição.')
else:
    print('O número 5 não foi encontrado.')
