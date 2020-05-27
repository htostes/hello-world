# Guardar valores em lista e mostrar maior e menor
num = list()
menores = list()
maiores = list()
for i in range(0, 5):
    num.append(int(input('Digite um número: ')))
maior = max(num)
menor = min(num)
for j, n in enumerate(num):
    if n == menor:
        menores.append(j)
    if n == maior:
        maiores.append(j)
print(f'O menor valor é {menor} e é encontrado em: {menores}')
print(f'O maior valor é {maior} e é encontrado em: {maiores}')
