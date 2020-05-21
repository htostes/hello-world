from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa de um triangulo com cateto oposto igual a {:.1f} e adjacente igual a {:.1f} é: {:.1f}'.format(co, ca, hip))

