# Listagem de preços com tuplas
lista = ('Pão', 3.88, 'Leite', 4.86, 'Rosca de Chocolate', 5.74, 'Passa-Tempo', 5.10, 'Suco Natural', 6.74,
         'Presunto', 4.20, 'Mussarela', 3.79, 'Peito de Peru', 5.40, 'Guaraná Antartica', 6.50)
print('-'*38)
print(f'{"Listagem de Preços":^38}')
print('-'*38)
for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<30}R${lista[i+1]:>6.2f}')
print('-'*38)
