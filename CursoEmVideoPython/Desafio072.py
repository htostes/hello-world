# número por extenso
extenso = ('zero', 'um', 'dois' , 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
esc = int(input('Digite um número (entre 0 e 20): '))
while esc < 0 or esc > 20:
    esc = int(input('Tente novamente (entre 0 e 20): '))
print(f'O número {esc} por extenso é {extenso[esc]}')
