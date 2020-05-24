# Primeiro menu
from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opc = '0'
while opc != '5':
    print('{:=^30}'.format(' \033[35mMenu\033[m '), end='')
    print("""
    O que deseja fazer?
    N1 = \033[34m{}\033[m --- N2 = \033[32m{}\033[m
    \033[31m[1]\033[m - SOMAR
    \033[31m[2]\033[m - MULTIPLICAR
    \033[31m[3]\033[m - MAIOR
    \033[31m[4]\033[m - NOVOS NÚMEROS
    \033[31m[5]\033[m - SAIR""".format(n1, n2))
    opc = str(input('Opção desejada: ')).strip()
    if opc == '1':
        print('SOMA = {:.1f} + {:.1f} = \033[33m{:.1f}\033[m'.format(n1, n2, n1+n2))
    elif opc == '2':
        print('MULTIPLICAÇÃO = {:.1f} * {:.1f} = \033[33m{:.1f}\033[m'.format(n1, n2, n1*n2))
    elif opc == '3':
        maior = n1
        if n2 > n1:
            maior = n2
        print('MAIOR: \033[33m{:.1f}\033[m'.format(maior))
    elif opc == '4':
        n1 = float(input('Digite o novo valor de n1: '))
        n2 = float(input('Digite o novo valor de n2: '))
    elif opc == '5':
        print('\033[34mAté logo!\033[m')
    else:
        print('\033[31mOpção inválida!\033[m')
    sleep(2)


