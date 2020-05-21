# Verificar possibilidade de formar um trinagulo e dizer qual o tipo de triangulo
r1 = float(input('Digite o primeiro segmento de reta: '))
r2 = float(input('Digite o segundo segmento de reta: '))
r3 = float(input('Digite o terceiro segmento de reta: '))
cond1 = (r1 + r2) > r3
cond2 = (r1 + r3) > r2
cond3 = (r2 + r3) > r1
if cond1 and cond2 and cond3:
    print('O triângulo \033[34mpode\033[m ser formado com as retas {:.1f} x {:.1f} x {:.1f}'
          .format(r1, r2, r3))
    if r1 == r2 and r2 == r3:
        print('E mais ainda, ele é \033[36mEQUILÁTERO\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('E mais ainda, ele é \033[36mISÓSCELES\033[m')
    else:
        print('E mais ainda, ele é \033[36mESCALENO\033[m')
else:
    print('O triangulo \033[31mnao pode\033[m ser formado com as retas {:.1f} x {:.1f} x {:.1f}'
          .format(r1, r2, r3))

