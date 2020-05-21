from random import sample
n1 = input('Nome do estudante: ')
n2 = input('Nome do estudante: ')
n3 = input('Nome do estudante: ')
n4 = input('Nome do estudante: ')
res = sample([n1, n2, n3, n4], 4)
print('{} vai primeiro, depois {}, em seguida {} e por ultimo {}'.format(res[0], res[1], res[2], res[3]))
