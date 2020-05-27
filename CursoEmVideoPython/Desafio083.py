expressao = str(input('Digite a expressão: ')).strip()
pilha = list()
for c in expressao:
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão digitada é válida!')
else:
    print('A expressão digitada é inválida!')
