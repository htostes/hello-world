frase = input('Digite uma frase: ')
frasef = frase.strip().upper()
print('Quantidade de \'A\': {}\n'
      'Primeira aparição: {}\n'
      'Ultima aparição: {}'.format(frasef.count('A'), frasef.find('A'), frasef.rfind('A')))
