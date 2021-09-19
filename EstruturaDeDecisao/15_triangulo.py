primeiroLado = float(input('Informe o primeiro lado do triângulo: '))
segundoLado = float(input('Informe o segundo lado do triângulo: '))
terceiroLado = float(input('Informe o terceiro lado do triângulo: '))

if primeiroLado > (segundoLado + terceiroLado) or segundoLado > (primeiroLado + terceiroLado) or terceiroLado > (primeiroLado + segundoLado):
    triangulo = False
else:
    triangulo = True

if triangulo:
    if primeiroLado == segundoLado and segundoLado == terceiroLado:
        print('Você formou um Triângulo Equilátero. Todos os lados são iguais.')

    elif primeiroLado == segundoLado or terceiroLado == primeiroLado or segundoLado == terceiroLado:
        print('Você formou um Triângulo Isóceles. Dois de seus lados são iguais.')

    else:
        print('Você formou um Triângulo Escaleno. Todos os lados são diferentes.')

else:
    print('Os 3 lados não formam um triângulo')