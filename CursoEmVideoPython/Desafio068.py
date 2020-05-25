# Jogo Par ou Impar
from random import randint
vitorias = 0
print(f'{" Par ou Ímpar ":~^30}')
while True:
    njog = int(input('Seu número: '))
    escJogador = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    npc = randint(0, 10)
    if ((npc + njog) % 2 == 0 and escJogador == 'P') or ((npc + njog) % 2 != 0 and escJogador == 'I'):
        print(f'Com: {npc} --- Jog: {njog}')
        print('Jogador Venceu!')
        vitorias += 1
    else:
        print(f'Com: {npc} --- Jog: {njog}')
        print('Computador Venceu!')
        break
    print('~-'*15)
print('~-'*15)
print(f'Vitórias consecutivas do jogador: {vitorias}')
