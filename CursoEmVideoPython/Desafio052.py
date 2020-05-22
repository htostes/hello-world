# verifica se o numero é primo
n = int(input('Digite o número para checar se é primo: '))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print('O número \033[34m{}\033[m é PRIMO'.format(n))
else:
    print('O número \033[31m{}\033[m NÃO É PRIMO'.format(n))
