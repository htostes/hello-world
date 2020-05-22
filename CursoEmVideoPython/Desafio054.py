from datetime import date
# Contador de maioridade
qntPessoas = int(input('Digite a quantidade de pessoas: '))
maior = 0
ano = date.today().year
for i in range(0, qntPessoas):
     nasc = int(input('Digite o ano de nascimento da pessoa {}: '.format(i+1)))
     if ano-nasc >= 21:
         maior += 1
print('Das \033[33m{}\033[m pessoas, \033[34m{}\033[m já atingiram a maioridade e \033[31m{}\033[m ainda não.'
      .format(qntPessoas, maior, qntPessoas-maior))
