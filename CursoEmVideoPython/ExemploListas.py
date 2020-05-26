# Exemplo de comandos com listas
lista = [2, 5, 7, 4]
print(lista)

# Mudando elementos
lista[0] = 8
print(lista, 'Mudou o elemento [0] para 9')

# Formas de adicionar elementos
lista.append(5)
print(lista, 'Adicionou o elemento 5 com append')
lista.insert(0, 9)  # Inseri na posição 0 o elemento 9
print(lista, 'Adicionou o elemento 9 com insert')

# Removendo elementos da lista
lista.remove(5) # Remove a primeira ocorrencia do elemento passado
print(lista, 'Retirou o primeiro elemento 5 da lista com remove')
lista.pop()  # Retira da lista o elemento do ultimo indice
print(lista, 'Retirou da lista com pop')
lista.pop(1)  # Retira da lista o elemento do indice passado
print(lista, 'Retirou da lista com pop passando indice 1')
del lista[1]  # Deleta o elemento de indice passado
print(lista, 'Deletou da lista o que estava no indice 1 com del')

# Ordenando
lista = [2, 8, 6, 9]
print(lista, 'Refiz a lista')
lista.sort()
print(lista, 'Sort')
lista.sort(reverse=True)
print(lista, 'Sort com reverse true')
