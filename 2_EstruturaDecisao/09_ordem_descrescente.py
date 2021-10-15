# Faça um Programa que leia três números e mostre-os em ordem decrescente.

primeiroNumero = float(input('Informe o primeiro número: '))
segundoNumero = float(input('Informe o segundo número: '))
terceiroNumero = float(input('Informe o terceiro número: '))

if primeiroNumero > segundoNumero:
    print(primeiroNumero)
    if segundoNumero > terceiroNumero:
        print(segundoNumero)
        print(terceiroNumero)
    else:
        print(terceiroNumero)
        print(segundoNumero)

elif segundoNumero > terceiroNumero:
    print(segundoNumero)
    if primeiroNumero > terceiroNumero:
        print(primeiroNumero)
        print(terceiroNumero)
    else:
        print(terceiroNumero)
        print(primeiroNumero)

else:
    print(terceiroNumero)
    if primeiroNumero > segundoNumero:
        print(primeiroNumero)
        print(segundoNumero)
    else:
        print(segundoNumero)
        print(primeiroNumero)