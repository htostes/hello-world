from datetime import date
pessoa = {'nome': str(input('Nome: ').strip()),
          'idade': date.today().year-int(input('Ano de nascimento: ')),
          'CTPS': int(input('CTPS (Só números): '))}
if pessoa['CTPS'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = int(input('Salario: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + 35 - (date.today().year - pessoa['contratacao'])
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')


