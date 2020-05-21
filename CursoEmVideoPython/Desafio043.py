# Calculo e classificação de IMC
alt = float(input('Digite sua altura em metros: '))
peso = float(input('Digite o seu peso em kg: '))
imc = peso / (alt * alt)
if imc < 18.5:
    print('Voce esta \033[33mabaixo do peso\033[m. IMC: \033[33m{:.1f}\033[m'
          .format(imc))
elif imc >= 18.5 and imc < 25:
    print('Voce esta no \033[34mpeso ideal\033[m. IMC: \033[34m{:.1f}\033[m'
          .format(imc))
elif imc >=25 and imc < 30:
    print('Voce esta com \033[33msobrepeso\033[m. IMC: \033[33m{:.1f}\033[m'
          .format(imc))
elif imc >=30 and imc < 40:
    print('Voce esta com \033[31mobesidade\033[m. IMC: \033[31m{:.1f}\033[m'
          .format(imc))
else:
    print('Voce esta com \033[31mobesidade morbida\033[m. IMC: \033[31m{:.1f}\033[m'
          .format(imc))
