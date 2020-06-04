pessoa = {'nome': str(input('Nome: ')).strip(), 'media': float(input(f'Média: '))}
print(f'O aluno {pessoa["nome"]} tem média {pessoa["media"]}')
if pessoa['media'] >= 7.0:
    print('E por isso está APROVADO.')
else:
    print('E por isso está REPROVADO.')
