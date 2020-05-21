# Conversão entre bases
# bin(i) retorna uma string com o numero inteiro i convertido para binario
# Idem para hex(i) e oct(i)

print('>'*10, 'Conversor de bases', '<'*10)
i = int(input('Digite um numero inteiro: '))
print('Opções:\n'
      '1 - Para Binario\n'
      '2 - Para Octal\n'
      '3 - Para Hexadecimal')
opc = str(input('Digite a opção desejada: ')).strip()

if opc is '1':
    print('{} na base 10 foi convertido para {} na base 2.'.format(i, bin(i)[2:]))
elif opc is '2':
    print('{} na base 10 foi convertido para {} na base 8.'.format(i, oct(i)[2:]))
elif opc is '3':
    print('{} na base 10 foi convertido para {} na base 16.'.format(i, hex(i)[2:]))
else:
    print('Opção invalida. Terminando o programa...')

