# NOTAS ALUNOS
# [[Nome, [n1, n2, media]], [Nome, [n1, n2, media]]]
dados = list()
notas = list()
alunos = list()
while True:
    dados.append(str(input('Nome: ')).strip())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    notas.append((notas[0]+notas[1])/2)
    dados.append(notas[:])
    alunos.append(dados[:])
    dados.clear()
    notas.clear()
    c = ' '
    while c not in 'SN':
        c = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    if c == 'N':
        break
print('-='*15)
print(f'No. {"Nome":<15}Média')
print('-'*30)
for i, aluno in enumerate(alunos):
    nome = aluno[0]
    media = aluno[1][2]
    print(f'{i:<4}{nome:<15}{media:>5.1f}')
while True:
    n = int(input('Deseja ver os dados de que aluno(999 interrompe): '))
    if n == 999:
        break
    if len(alunos) > n >= 0:
        print(f'Notas de {alunos[n][0]} são {alunos[n][1][0:2]}')
    else:
        print('Aluno inválido.')
