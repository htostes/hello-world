from random import randint

print('Olá Dave, vou pensar em um numero entre 0 e 5, tente adivinhar.')
adv = randint(0, 5)
i = int(input('Pensei, agora tente adivinhar: '))
if i in [0, 1, 2, 3, 4, 5]:
    if adv == i:
        print('Boa Dave, voce tinha {:.2f}% de chance de acerto e mesmo assim conseguiu.'
              .format(1 / 6 * 100))
    else:
        print('Que pena Dave, eu tinha {:.2f}% de vencer e venci. Pensei em {}.'
              .format(5 / 6 * 100, adv))
else:
    print('Era para ser entre 0 e 5 Dave. Talvez eu tenha te superestimado.')
