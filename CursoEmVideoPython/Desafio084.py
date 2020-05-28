dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Digite o Nome: ')).strip())
    dados.append(float(input('Digite o Peso: ')))
    if len(pessoas) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] < menor:
            menor = dados[1]
        if dados[1] > maior:
            maior = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('-'*30)
    if c == 'N':
        break
print(f'Cadastrados: {len(pessoas)}')
print('Pessoas mais pesadas: ', end='')
for i in pessoas:
    if i[1] == maior:
        print(i[0], end=' - ')
print('\nPessoas mais leves: ', end='')
for i in pessoas:
    if i[1] == menor:
        print(i[0], end=' - ')
