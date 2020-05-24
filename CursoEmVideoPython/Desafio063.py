# Fibonacci
print('{:=^40}'.format(' Fibonacci '))
i = int(input('Quantos termos de fibonacci: '))
n1 = 0
n2 = 1
if i > 0:
    print('[ {} '.format(n1), end='')
    if i > 1:
        print('{} '.format(n2), end='')
    if i > 2:
        while i > 2:
            n = n1 + n2
            n1 = n2
            n2 = n
            i -= 1
            print(n, end=' ')
    print(']')


