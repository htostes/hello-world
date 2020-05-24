r = 'S'
qnt = 0
soma = 0
while r == 'S':
    n = int(input('Digite o número: '))
    qnt += 1
    if qnt == 1:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()
print("""
A média dos valores inseridos: \033[32m{:.2f}\033[m
O maior valor: \033[34m{}\033[m
O menor valor: \033[31m{}\033[m""".format(soma/qnt, maior, menor))
