# Progressão Aritmética com While
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
i = 1
print('Os primeiros 10 termos dessa PA são')
print('[ ', end='')
while i <= 10:
    print('{} '.format(p), end='')
    p += r
    i += 1
print(']')
