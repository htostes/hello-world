from time import sleep
import emoji
# Fogos de artificio
input('Pronto para os fogos!?')
for i in range(10, -1, -1):
    sleep(1)
    print('\033[33m', i, '\033[m')
print('{:{}^30}'.format('Fooogos !!', emoji.emojize(':fire:')))

