# Verifica alistamento militar
from datetime import date
print('='*10, 'Serviço Militar', '='*10)
nasc = int(input('Digite o ano de nascimento do jovem: '))
ano = date.today().year
idade = int(ano) - nasc
if idade < 18:
    print('Voce ainda não precisa se alistar. Volte em \033[34m{} anos\033[m'.format(18-idade))
elif idade > 18:
    print('Voce ja deveria ter se alistado. Tempo de atraso: \033[31m{} anos\033[m'.format(idade-18))
else:
    print('\033[36mÉ hora de se alistar!\033[m')