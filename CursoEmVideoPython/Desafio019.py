from random import choice
n1 = input('Nome do 1º aluno(a): ')
n2 = input('Nome do 2º aluno(a): ')
n3 = input('Nome do 3º aluno(a): ')
n4 = input('Nome do 4º aluno(a): ')
escolhido = choice([n1, n2, n3, n4])
print('{} vai lá apagar o quadro.'.format(escolhido))
