# Vogais em palavras da tupla
tupla = ('PAO', 'LEITE', 'ROSCA', 'BOLACHA', 'SUCO', 'PRESUNTO', 'MUSSARELA', 'GUARANA')
for i, palavra in enumerate(tupla):
    print(f'Na palavra {palavra} temos as vogais ', end='')
    for j in tupla[i]:
        if j in 'AEIOU':
            print(f'{j}', end=' ')
    print()
