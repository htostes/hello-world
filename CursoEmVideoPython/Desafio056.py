# Informações de um grupo de pessoas
qnt = int(input('Digite a quantidade de pessoas: '))
somaIdade = 0
maior = 0
mulheres = 0
nomeMaior = ''
for i in range(0, qnt):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i+1))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i+1)))
    somaIdade += idade
    sexo = str(input('Digite o sexo (Masculino ou Feminino) da {}ª pessoa: '
                     .format(i+1))).strip().lower()
    if sexo[0:3] == 'mas' and idade > maior:
        maior = idade
        nomeMaior = nome
    if sexo[0:3] == 'fem' and idade < 20:
        mulheres += 1
print('Media: {:.1f}'.format(somaIdade/qnt))
print('Mulheres < 20 anos: {}'.format(mulheres))
print('Homem mais velho: {}'.format(nomeMaior))
