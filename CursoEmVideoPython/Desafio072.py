# número por extenso
extenso = ('zero', 'um', 'dois' , 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    esc = int(input('Digite um número (entre 0 e 20): '))
    if 20 >= esc >= 0:
        break
print(f'O número {esc} por extenso é {extenso[esc]}')
