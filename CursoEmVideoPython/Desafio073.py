# Informações da tupla
jogadores = ('Theoretical', 'illsory', 'DenBut', 'UchihaSaske', 'SCACC', 'Thund3r', 'Flix', 'Blastoise', 'trahison',
             'Hawkeye', 'Ryan223437', 'Ostkaka', 'Leta', 'Ethan', 'bobbyex', 'Enori', 'ThaLucky1', 'FAST44', 'matff',
             'Monsanto')
# 5 primeiros colocados
print(f'Os cinco primeiro colocados: {jogadores[:5]}')
# Os ultimos 4 colocados
print(f'Os últimos 4 colocados: {jogadores[-4:]}')
# Ordem alfabética
print(f'Jogadores em ordem alfabética: {sorted(jogadores)}')
# Posição de um jogador específico
print(f'O jogador Blastoise está na {jogadores.index("Blastoise")+1}ª posição.')