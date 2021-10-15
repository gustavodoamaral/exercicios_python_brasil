valorSaque = int(input('Notas disponíveis: 1, 5, 10, 50 e 100 \nInforme o valor de saque [Min.: 10 - Máx.: 600]: '))

if (valorSaque < 10) or (valorSaque > 600):
    print('Valor invalido para saque')
else:
    notaCem = int(valorSaque / 100)
    notaCinquenta = int((valorSaque - (notaCem * 100)) / 50)
    notaDez = int((valorSaque - (notaCem * 100) - (notaCinquenta * 50)) / 10)
    notaCinco = int((valorSaque - (notaCem * 100) - (notaCinquenta * 50) - (notaDez * 10)) / 5)
    notaUm = valorSaque - (notaCem * 100) - (notaCinquenta * 50) - (notaDez * 10) - (notaCinco * 5)

print (f'Notas de 100: {notaCem}')
print (f'Notas de  50: {notaCinquenta}')
print (f'Notas de  10: {notaDez}')
print (f'Notas de   5: {notaCinco}')
print (f'Notas de   1: {notaUm}')