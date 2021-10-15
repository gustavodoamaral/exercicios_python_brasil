primeiroNumero = float(input('Informe o primeiro número: '))
segundoNumero = float(input('Informe o segundo número: '))

if primeiroNumero > segundoNumero:
    print(f'{primeiroNumero} é o maior número')
elif primeiroNumero < segundoNumero:
    print(f'{segundoNumero} é o maior número')
else:
    print('Os número são iguais')