# Guardar valores em tupla

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o ultimo numero: '))
valores = (n1, n2, n3, n4)
print(f'Os valores inseridos foram: \033[34m{valores}\033[m')
print(f'O número 9 apareceu \033[32m{valores.count(9)}\033[m vezes')
if 3 in valores:
    print(f'O valor 3 apareceu pela primeira vez na \033[31m{valores.index(3)+1}ª\033[m posição')
else:
    print('O valor 3 não foi encontrado')
print('Os valores pares digitados foram: [',end=' ')
for i in valores:
    if i % 2 == 0:
        print(f'{i}', end=' ')
print(']')
