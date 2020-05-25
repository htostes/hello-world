# Mostra tabuadas
print(f'{" TABUADAS ":=^30}')
while True:
    i = int(input('Digite o número para ver a tabuada (Negativo para parar): '))
    if i < 0:
        print('\nObrigado e até logo!')
        break
    else:
        print(f'{f"Tabuada do {i}":~^30}')
        for j in range(1, 11):
            print(f'{f"{i} x {j} = {i*j}":^30}')
        print('~'*30)