#rad * 180 / pi = ang <--> rad = ang / 180 * pi
import math
ang = float(input('Digite o angulo: '))
rad = (ang/180)*math.pi
sen = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)
print('{:<10}: {:<4.1f}'.format('Angulo', ang))
print('{:<10}: {:<4.1f}'.format('Radiano', rad))
print('{:<10}: {:<4.3f}'.format('Cosseno', cos))
print('{:<10}: {:<4.3f}'.format('Seno', sen))
print('{:<10}: {:<4.3f}'.format('Tangente', tang))
