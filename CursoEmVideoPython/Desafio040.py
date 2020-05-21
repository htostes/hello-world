# Média simples de nota
n1 = float(input('Digite a primeira nota do estudante: '))
n2 = float(input('Digite a segunda nota do estudante: '))
media = (n1 + n2) / 2

if media < 5:
    print('\033[31mREPROVADO\033[m. Media final: \033[31m{:.1f}\033[m'.format(media))
elif media >= 7:
    print('\033[34mAPROVADO\033[m. Media final: \033[34m{:.1f}\033[m'.format(media))
else:
    print('\033[32mRECUPERAÇÃO\033[m. Media final: \033[32m{:.1f}\033[m'.format(media))
