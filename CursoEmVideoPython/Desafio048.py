# Programa que calcula a soma de todos os
# numeros impares e multiplos de 3 em um intervalo

i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
s = 0
for n in range(i, f+1):
    if n % 2 != 0 and n % 3 == 0:
        print(n, '+ ', end='')
        s += n
print('\n\033[1mSoma =\033[m \033[35m{}\033[m'.format(s))