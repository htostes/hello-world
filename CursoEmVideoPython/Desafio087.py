matriz = [[], [], []]
spares = s3coluna = maior2linha = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Valor da casa [{i}][{j}]: ')))
print('='*30)
for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            spares += matriz[i][j]
        if j == 2:
            print(f'[{matriz[i][j]:^3}]')
            s3coluna += matriz[i][j]
        else:
            print(f'[{matriz[i][j]:^3}]', end='')
print('='*30)
print(f'Soma dos pares na matriz: {spares}')
print(f'Soma da 3ª coluna: {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print(f'Maior da 2ª linha: {max(matriz[1])}')
