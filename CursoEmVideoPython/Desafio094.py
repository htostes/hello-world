pessoa = dict()
geral = list()
mulheres = list()
velhos = list()
media = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    geral.append(pessoa.copy())
    c = ' '
    while c not in 'SN':
        c = str(input('Continua? [S/N]: ')).strip().upper()
    if c == 'N':
        break
for i in geral:
    media += i['idade']
    if i['sexo'] == 'F':
        mulheres.append(i['nome'])
media /= len(geral)
for i in geral:
    if i['idade'] > media:
        velhos.append(i['nome'])

print('{:=^30}'.format(' DADOS '))
print(f'Foram cadastrados {len(geral)} pessoas.')
print(f'A média das idades: {media:.1f}')
print(f'Lista com todas mulheres: {mulheres}')
print(f'Lista com todas pessoas com idade acima da média: {velhos}')
