primeiroNumero = float(input('Informe o primeiro número: '))
segundoNumero = float(input('Informe o segundo número: '))
terceiroNumero = float(input('Informe o terceiro número: '))

if primeiroNumero == segundoNumero and primeiroNumero == terceiroNumero:
    print('Os números são iguais')

elif primeiroNumero > segundoNumero and primeiroNumero > terceiroNumero:
    print(f'{primeiroNumero} é o maior número')

elif segundoNumero > terceiroNumero:
    print(f'{segundoNumero} é o maior número')

else:
    print(f'{terceiroNumero} é o maior numero')

if primeiroNumero == segundoNumero and primeiroNumero == terceiroNumero:
    print('Os números são iguais')

elif primeiroNumero < segundoNumero and primeiroNumero < terceiroNumero:
    print(f'{primeiroNumero} é o menor número')

elif segundoNumero < terceiroNumero:
    print(f'{segundoNumero} é o menor número')

else:
    print(f'{terceiroNumero} é o menor numero')