# Classificação da categoria de natação
from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
ano = int(date.today().year)
idade = ano - nasc
if idade <= 9:
    print('A classificação do atleta é \033[31mMIRIM')
elif idade > 9 and idade <= 14:
    print('A classificação do atleta é \033[32mINFANTIL')
elif idade > 14 and idade <= 19:
    print('A classificação do atleta é \033[33mJUNIOR')
elif idade > 19 and idade <= 20:
    print('A classificação do atleta é \033[34mSÊNIOR')
else:
    print('A classificação do atleta é \033[35mMASTER')
