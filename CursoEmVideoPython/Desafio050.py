# Soma dos valores pares que o usario digitar
s = 0
for i in range(0, 6):
    n = int(input('Digite o número: '))
    if n % 2 == 0:
        s += n
print('A soma dos valores \033[31mPARES\033[m digitados foi de: \033[1;32m{}\033[m'.format(s))
