# Números aleatorios em tuplas
from random import randint

aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números aleatorios gerados foram: \033[35m{aleatorios}\033[m')
menor = maior = aleatorios[0]
for i in aleatorios:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print(f'O \033[31mmenor\033[m valor da tupla é: \033[31m{menor}\033[m')
print(f'O \033[34mmaior\033[m valor da tupla é: \033[34m{maior}\033[m')