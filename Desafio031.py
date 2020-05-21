v = float(input('Quantos km tem sua viagem: '))
if v > 200.0:
    preco = v * 0.45
else:
    preco = v * 0.50
print('O preco para uma passagem de {}km é de R${:.2f}'.format(v, preco))
