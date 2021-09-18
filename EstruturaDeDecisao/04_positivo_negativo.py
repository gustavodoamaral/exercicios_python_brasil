numero = float(input('Informe um número: '))

if numero > 0:
    print(f'{numero} é um número positivo')
elif numero < 0:
    print(f'{numero} é um número negativo')
elif numero == 0:
    print(f'{numero} é um número neutro')