frase = " Olha que coisa mais linda "

print('frase == {}'.format(frase))
print('#frase[3] == {}'.format(frase[3]))                   # caracter 3
print('#frase[9:] == {}'.format(frase[9:]))                 # de 9 ate o fim
print('#frase[9:14] == {}'.format(frase[9:14]))             # de 9 ate 13
print('#frase[9::2] == {}'.format(frase[9::2]))             # de 9 ate o fim pulando 2
print('#frase[9:19:2] == {}'.format(frase[9:19:2]))         # de 9 ate 18 pulando 2
print('#frase[::3] == {}'.format(frase[::3]))               # de inicio ate fim pulando 3
print('#len(frase) == {}'.format(len(frase)))               # nro de caracteres
print('#frase.strip() == {} #Novo len {}'
      .format(frase.strip(), len(frase.strip())))           # tira espacos a direita e a esquerda
print('#frase.count(\'a\') == {}'.format(frase.count('a'))) # conta quantos 'a'
print('#frase.count(\'A\') == {}'.format(frase.count('A'))) # conta quantos 'A'
print('#frase.upper().count(\'A\') == {}'
      .format(frase.upper().count('A')))                    # conta quantos 'A' depois de jogar a frase toda pra maiuscula
print('#frase.replace(\'linda\',\'graça\') == {}'
      .format(frase.replace('linda', 'graça')))             # troca a primeira palavra pela segunda, todas as ocorrencias
print('#\'coisa\' in frase == {}'.format('coisa' in frase)) # Verifica se existe coisa em frase
print('#frase.find(\'linda\') == {}'
      .format(frase.find('linda')))                         # retorna o indice da primeira letra ou caso nao tenha -1
print('#frase.count(\'linda\') == {}'
    .format(frase.count('linda')))                          # retorna a qnt de linda na frase
print('#frase.split() == {}'
    .format(frase.split()))                                 # retorna uma lista com as palavras divididas



print("""\nOlha o tamanho dessa jamanta
é muito gigante, parece um mamute
ainda bem que é só um elefante.
Eu nao estou falando de um ser humano,
seu doente.""")  # Para escrever textos grandes usa-se tres aspas
