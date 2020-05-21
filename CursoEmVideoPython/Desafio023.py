snum = input('Digite um numero inteiro entre 0 e 9999: ')
snum = snum.strip()
snum = '{:0>4}'.format(snum)
print(snum)
inum = int(snum)

# Solucao por matematica
milhar = int(inum/1000)
centena = int((inum / 100) - (milhar * 10))
dezena = int((inum/10) - (milhar * 100) - (centena * 10))
unidade = int(inum - (milhar*1000) - (centena * 100) - (dezena * 10))

print('#Solução Matematica:\n'
      'Milhar:  {}\n'
      'Centena: {}\n'
      'Dezena:  {}\n'
      'Unidade: {}'.format(milhar, centena, dezena, unidade))

# Solucao por string
milhar = snum[0]
centena = snum[1]
dezena = snum[2]
unidade = snum[3]
print('#Solução String:\n'
      'Len: {}\n'
      'Milhar:  {}\n'
      'Centena: {}\n'
      'Dezena:  {}\n'
      'Unidade: {}'.format(len(snum), milhar, centena, dezena, unidade))
