jogador = {'nome': str(input('Nome: ')).strip(),
           'gols': [],
           'total': 0}
partidas = int(input(f'Quantos partidas {jogador["nome"]} jogou: '))
for i in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na {i+1}ª partida: ')))
jogador['total'] = sum(jogador['gols'])
print('-='*15)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print('=-'*15)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, qnt in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {qnt} gols.')
print(f'Com isso foi um total de {jogador["total"]} gols.')
