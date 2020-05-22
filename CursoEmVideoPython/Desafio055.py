# Ler pesos e dizer qual o maior e qual o menor
qnt = int(input('Digite a quantidade de pessoas: '))
maior = float(input('Digite o peso da 1ª pessoa (kg): '))
menor = maior
for i in range(1, qnt):
    peso = float(input('Digite o peso da {}ª pessoa (kg): '.format(i+1)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('Dessas pessoas o maior peso foi \033[31m{:.1f}kg\033[m, e o menor foi \033[32m{:.1f}kg\033[m.'
      .format(maior, menor))
