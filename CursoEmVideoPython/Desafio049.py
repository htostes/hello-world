# Tabuada
n = int(input('Digite o numero que voce quer ver a tabuada: '))
print('\033[1m{:=^30}\033[m'.format('Tabuada do '+str(n)))
for i in range(1, 11):
    print('\033[31m{}\033[m x \033[32m{:<2}\033[m = \033[34m{}\033[m'.format(n, i, n*i))
