salario = float(input('Digite o salario: R$'))
if salario <= 1250:
    salario = salario * 1.15
else:
    salario = salario * 1.10
print('O novo salario é R${:.2f}'.format(salario))

