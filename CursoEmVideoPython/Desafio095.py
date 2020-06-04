jogadores = list()
while True:
    jogador = {'nome': str(input('Nome: ')).strip(),
               'gols': [],
               'total': 0}
    partidas = int(input(f'Quantos partidas {jogador["nome"]} jogou: '))
    for i in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na {i+1}ª partida: ')))
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    c = ' '
    while c not in 'SN':
        c = str(input('Continuar? [S/N]: ')).strip().upper()
    print('-='*15)
    if c == 'N':
        break
print(f'No. {"Nome":10} {"Gols":15} Total')
print('-'*38)
for i, jog in enumerate(jogadores):
    print(f'{i}   {jog["nome"]:10} {str(jog["gols"]):15} {jog["total"]}')
print('-'*38)
while True:
    opc = int(input('Dados de qual jogador? (999 interrompe): '))
    if opc == 999:
        break
    elif len(jogadores) > opc >= 0:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opc]["nome"]}')
        for i, qnt in enumerate(jogadores[opc]['gols']):
            print(f'    => Na partida {i + 1}, fez {qnt} gols.')
        print(f'Com isso foi um total de {jogadores[opc]["total"]} gols.')
        print('-'*38)
    else:
        print('Jogador não encontrado.')
        print('-'*38)


