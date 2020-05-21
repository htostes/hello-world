from math import ceil
v = float(input('Qual a velocidade atual do carro: '))
if v > 80.0:
    #multa = int(ceil(v - 80)) * 7
    multa = (v - 80) * 7
    print('Voce esta acima do limite de 80km/h, voce ira receber uma multa de R${:.2f}.'
          .format(multa))
else:
    print('Voce esta dentro dos limites de velocidade.')