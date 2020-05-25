soma = count = 0
while True:
    i = int(input('Digite o número [Para parar digite 999]: '))
    if i == 999:
        break
    soma += i
    count += 1
print(f'Foram digitados \033[32m{count}\033[m números e a soma deles é \033[33m{soma}\033[m')
print('Até mais!')
