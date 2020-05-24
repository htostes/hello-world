
n = int(input('Digite um numero: '))
qnt = 0
soma = 0
while n != 999:
    soma += n
    qnt += 1
    n = int(input('Digite outro número (O programa para se digitar 999): '))
print('Foram digitados \033[34m{}\033[m números\nE a soma é \033[32m{}\033[m'.format(qnt, soma))
