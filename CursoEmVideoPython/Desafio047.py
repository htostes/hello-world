# Verifica numeros pares em um intervalo
i = int(input('Digite o primeiro número: '))
f = int(input('Digite o ultimo número: '))
for n in range(i, f+1):
    if n % 2 == 0:
        print(n, ' ', end='')
print('\nTodos esses números são \033[34mPARES\033[m.')


