# Fatorial
print('{:=^40}'.format(' FATORIAL '))
n = int(input('Digite o numero que deseja ver o fatorial: '))
print('O fatorial de {} é: '.format(n), end='')
fat = 1
while n != 0:
    if n != 1:
        print(n, end=' x ')
    else:
        print(n, end=' = ')
    fat = fat * n
    n = n - 1
print(fat)
