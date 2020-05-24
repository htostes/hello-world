# Progressão Aritmética com While, 061 melhorado
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
i = 10
print('[ ', end='')
while i >= 1:
    print('{} '.format(p), end='')
    p += r
    i -= 1
    if i == 0:
        i = int(input('\nDeseja ver mais quantos termos? '))
print(']')
