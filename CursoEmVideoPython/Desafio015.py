# Pagar po dia alugado R$60 e por km rodado R$0.15
dia = int(input('Quantos dias voce rodou: '))
km = float(input('Quantos km foram rodados: '))
total = (dia*60) + (km*0.15)
print('O total a pagar apos rodar por {} dias e andar {:.1f}km é: R${:.2f}'.format(dia, km, total))
