from random import randint
# Jogo da adivinhação
print('\033[36m{:=^40}\033[m'.format(' Jogo da Adivinhação '))
print('Sou eu de novo Dave, dessa vez vou pensar em um número de 0 a 11')
print('Vamos ver quantas tentativas leva para voce acertar.')
pc = randint(0, 10)
jog = int(input('Já pensei, agora tente adivinhar (Chance de acerto \033[34m{:.2f}%\033[m): '
                .format((1/11)*100)))
cont = 1
while pc != jog:
    print('Errou Dave, sua chance agora é de \033[34m{:.2f}%\033[m'.format((1/(11-cont)*100)))
    jog = int(input('Tente de novo Dave: '))
    cont += 1
print('Muito bem Dave, levou \033[32m{}\033[m tentativas para conseguir adivinhar que eu tinha pensado em {}.'
      .format(cont, pc))
