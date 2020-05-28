matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Valor da casa [{i}][{j}]: ')))
print(matriz)
for i in range(0, 3):
    for j in range(0, 3):
        if j == 2:
            print(f'[{matriz[i][j]:^3}]')
        else:
            print(f'[{matriz[i][j]:^3}]', end='')
