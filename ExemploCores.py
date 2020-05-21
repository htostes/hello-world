print('\033[7;30mBom dia familia!\033[m')  # 3 cor do texto - 4 cor do fundo
print('\033[1;30;41mBom dia familia!\033[m')  # x0 = branco
print('\033[4;31;40mBom dia familia!\033[m')  # x1 = vermelho
print('\033[3;30;42mBom dia familia!\033[m')  # x2 = verde
print('\033[0;30;43mBom dia familia!\033[m')  # x3 = amarelo
print('\033[0;30;44mBom dia familia!\033[m')  # x4 = azul
print('\033[0;30;45mBom dia familia!\033[m')  # x5 = roxo
print('\033[0;30;46mBom dia familia!\033[m')  # x6 = ciano
print('\033[1;30;47mBom dia familia!\033[m')  # x7 = cinza
print('Bom dia minha {}{}{} !'.format('\033[1;36m', 'família', '\033[0m'))

# Dicionario de cores
cores = {'limpo':'\033[m',
         'azul':'\033[1;34m',
         'vermelho':'\033[1;31m'}

print('Bom {}Dia{} minha {}Familia{}!'
      .format(cores['azul'], cores['limpo'], cores['vermelho'], cores['limpo']))
