todos = list()
while True:
    todos.append(int(input('Digite o numero: ')))
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if c == 'N':
        break
pares = list()
impares = list()
for n in todos:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Toda a lista:       {todos}\n'
      f'Números pares:      {pares}\n'
      f'Números ímpares:    {impares}')
