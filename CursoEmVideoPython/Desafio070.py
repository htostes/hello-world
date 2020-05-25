# Ler produtos

print('-='*15)
print(f'{" Loja do Barato ":=^30}')
print('-='*15)
caros = total = 0
primeira = True
while True:
    c = ' '
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        caros += 1
    if primeira:
        menor = preco
        nomeMenor = nome
        primeira = False
    elif preco < menor:
        menor = preco
        nomeMenor = nome
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-='*15)
    if c == 'N':
        break
print(f"""{' Fim da compra ':~^30}
Total: R${total:.2f}
Produto mais barato: {nomeMenor}
Produtos > R$1000.00: {caros}""")
