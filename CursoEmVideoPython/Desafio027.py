nome = input('Digite o nome: ')
nome = nome.strip().split()
print('Primeiro nome:   {}\n'
      'Ultimo nome:     {}'.format(nome[0], nome[len(nome)-1]))
