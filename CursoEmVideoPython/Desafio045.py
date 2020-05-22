from time import sleep
from random import choice

# Jokenpo
desenho = {'pedra': '--[]',
           'tesoura': '--<',
           'papel': '--E'}
print('-=-' * 5, '\033[35mJogo - Jokenpo\033[m', '-=-' * 5)
print('Vamos jogar Jokenpo. Escolha o seu, prometo que nao vou olhar.')
jog = str(input('Escreva pedra, papel ou tesoura: ')).strip().lower()
if jog != 'pedra' and jog != 'papel' and jog != 'tesoura':
    print('Voce nao sabe brincar...')
    exit()
pc = choice(['pedra', 'papel', 'tesoura'])
sleep(1)
print('\033[31mJo\033[m')
sleep(1)
print('\033[33mKen\033[m')
sleep(1)
print('\033[35mPo!\033[m')
if pc == jog:
    print('\033[31m{}\033[m  vs  \033[34m{}\033[m  Parece que foi um empate!'
          .format(desenho[pc], desenho[jog]))
elif pc == 'pedra' and jog == 'tesoura':
    print('\033[31m{}\033[m  vs  \033[34m{}\033[m  Ha! eu venci, humano!'
          .format(desenho[pc], desenho[jog]))
elif pc == 'tesoura' and jog == 'papel':
    print('\033[31m{}\033[m  vs  \033[34m{}\033[m  Ha! eu venci, humano!'
          .format(desenho[pc], desenho[jog]))
elif pc == 'papel' and jog == 'pedra':
    print('\033[31m{}\033[m  vs  \033[34m{}\033[m  Ha! eu venci, humano!'
          .format(desenho[pc], desenho[jog]))
else:
    print('\033[31m{}\033[m  vs  \033[34m{}\033[m Parece que voce me venceu, humano.'
          .format(desenho[pc], desenho[jog]))
