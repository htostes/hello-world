# Checa palindromo
original = str(input('Digite a frase: ')).strip().lower()
frase = original.replace(' ', '')
lfrase = len(frase)
palindromo = True
for i in range(0, int(lfrase/2).__trunc__()):
    if frase[i] != frase[lfrase-i-1]:
        palindromo = False
if palindromo:
    print('A frase "{}" \033[34mÉ um palindromo\033[m'.format(original))
else:
    print('A frase "{}" \033[31mNÃO É um palindromo\033[m'.format(original))
