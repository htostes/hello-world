numeros = list()
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0:  # primeira iteração
        numeros.append(num)
    else:
        lugar = i
        for j in range(i-1, -1, -1):  # olha a lista de tras pra frente
            if num < numeros[j]:  # se num for menor que numero[j], num toma seu lugar na lista
                lugar = j
            else:
                break
        numeros.insert(lugar, num)
    print(numeros)
