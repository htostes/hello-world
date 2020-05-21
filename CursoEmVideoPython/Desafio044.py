# Condição de pagamento
print('=-='*5, 'PAGAMENTO', '=-='*5)
preco = float(input('Digite o preço do produto: R$'))
print('Escolha a forma de pagamento...\n'
      '\033[34m1\033[m - Á vista dinheiro/cheque\033[34m(10% de desconto)\033[m\n'
      '\033[34m2\033[m - Á vista no cartão\033[34m(5% de desconto)\033[m\n'
      '\033[34m3\033[m - Á prazo em 2x no cartão\n'
      '\033[34m4\033[m - Á prazo em 3x ou mais no cartão\033[31m(20% de juros)\033[m')
opc = str(input('Digite o numero da opção: ')).strip()

if opc is '1':
    preco = preco * 0.9
    print('Preço a vista dinheiro/cheque: \033[32mR${:.2f}\033[m'.format(preco))
elif opc is '2':
    preco = preco * 0.95
    print('Preço a vista no cartão: \033[32mR${:.2f}\033[m'.format(preco))
elif opc is '3':
    print('Preço total a prazo em 2x: \033[32mR${:.2f}\033[m'.format(preco))
elif opc is '4':
    preco = preco * 1.2
    print('Preço total a prazo em 3x ou mais: \033[32mR${:.2f}\033[m'.format(preco))
else:
    print('Opção \033[31minválida\033[m. Terminando...')
print('=-='*14)


