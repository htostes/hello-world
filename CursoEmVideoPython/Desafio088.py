from random import randint
from time import sleep
# Sorteio Mega Sena
jogos = list()
jogo = list()
print('{:=^30}'.format(' SORTEIO MEGA SENA '))
qnt = int(input('Quantos jogos: '))
print(f'{" SORTEANDO ":=^30}')
for i in range(0, qnt):
    while len(jogo) < 6:
        aleatorio = randint(1, 60)
        if aleatorio not in jogo:
            jogo.append(aleatorio)
    jogo.sort()
    jogos.append(jogo[:])
    print(f'Jogo {i+1:>2}: {jogo}')
    sleep(1)
    jogo.clear()
print('-='*15)
