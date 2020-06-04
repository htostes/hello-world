from random import randint
from time import sleep
input('Start?')
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('-> JOGADAS <-')
for k, v in jogo.items():
    print(f'    O {k} tirou {v} no dado.')
    sleep(0.5)
# ORDENANDO O DICIONARIO 'JOGO'
temp = dict()
temp = jogo.copy()
jogo.clear()
while len(temp) > 0:
    k_maior = v_maior = max(temp.values())
    for k, v in temp.items():
        if v == v_maior:
            k_maior = k
            break
    jogo[k_maior] = v_maior
    temp.pop(k_maior)
# FIM DA ORDENAÇÃO
print('-> RANKING <-')
i = 1
for k, v in jogo.items():
    print(f'    {i}º Lugar: {k} com {v}')
    i += 1
    sleep(0.5)


