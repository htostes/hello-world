# Progressão Aritmética
inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Os \033[34mDEZ\033[m primeiros termos dessa PA são: ')
for n in range(inicio, inicio+(razao * 10), razao):
    print(n, ' ', end='')
