# Cadastro de pessoas

print('=-'*15)
print(f'{"Cadastro de Pessoas":^30}')
print('-='*15)
maior = homem = jovem = 0

while True:
    s = continua = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if s == 'M':
        homem += 1
    if s == 'F' and idade < 20:
        jovem += 1
    print('-='*15)
    if continua == 'N':
        break
print(f"""{'Dados Cadastrados':~^25}
Maiores de 18: {maior}
Mulheres jovens: {jovem}
Homens: {homem}""")
print('~'*25)
print('Obrigado. Até logo!')
