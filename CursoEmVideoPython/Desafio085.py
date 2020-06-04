numeros = [[], []]  # 0 sao pares, 1 são impares
for i in range(0, 7):
    num = int(input('Digite o numero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print('-'*30)
numeros[0].sort()
numeros[1].sort()
print(f'Pares: {numeros[0]}\nImpares: {numeros[1]}')
