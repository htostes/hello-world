# Empréstimo bancário
print('='*52)
print('='*10, 'Sistema de empréstimo bancário', '='*10)
print('='*52)
valor = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salario: R$'))
anos = int(input('Em quantos anos voce pretende pagar: '))
meses = anos * 12
prestacao = valor/meses
if(prestacao > (salario * 0.3)):
    print('Seu empréstimo foi negado pois a prestação excedeu o limite.\n'
          'Prestação: {:.2f}'.format(prestacao))
else:
    print('Seu empréstimo foi aceito.\n'
          'Prestação: {:.2f}\n'
          'Meses: {}.'.format(prestacao, meses))
