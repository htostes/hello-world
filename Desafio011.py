altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura*largura
print('Para pintar uma parede {:.1f}m x {:.1f}m, com area {:.1f}m^2 voce vai precisar de {:.1f}l de tinta'.format(altura, largura, area, area/2))
