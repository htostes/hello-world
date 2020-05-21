nome = input('Digite seu nome completo: ')
nome = nome.strip()
nomecaps = nome.upper()
nomesemcaps = nome.lower()
qntletras = int(len(nome)) - int(nome.count(' '))
qnt1nome = len(nome.split().__getitem__(0))
print('Nome em caps:                {}\n'
      'Nome sem caps:               {}\n'
      'Quantidade de letras:        {}\n'
      'Qnt de letras primeiro nome: {}'.format(nomecaps, nomesemcaps, qntletras, qnt1nome))