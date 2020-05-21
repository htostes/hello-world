import math
r1 = float(input('Digite o comprimento de r1: '))
r2 = float(input('Digite o comprimento de r2: '))
r3 = float(input('Digite o comprimento de r3: '))
cond1 = (r1 + r2) > r3
cond2 = (r2 + r3) > r1
cond3 = (r1 + r3) > r2
if cond1 and cond2 and cond3:
    print('É possível construir um triangulo de lados {:.1f} x {:.1f} x {:.1f}'
          .format(r1, r2, r3))
else:
    print('Não é possível construir um triangulo com os lados {:.1f} x {:.1f} x {:.1f}'
          .format(r1, r2, r3))
