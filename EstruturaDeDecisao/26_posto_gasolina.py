combustivel = str(input('[A] Alcool ou [G] Gasolina: '))
quantidadeLitros = int(input('Informe a quantidade de litros: '))

valorLitroG = 2.50
valorLitroA = 1.90

if combustivel == 'A':
    if quantidadeLitros <= 20:
        desconto = quantidadeLitros * 3
        valorLitroA = valorLitroA * quantidadeLitros
        valorTotal = valorLitroA - (valorLitroA * (desconto/100))

    elif quantidadeLitros > 20: 
        desconto = quantidadeLitros * 5
        valorLitroA = valorLitroA * quantidadeLitros
        valorTotal = valorLitroA - (valorLitroA * (desconto/100))


if combustivel == 'G':
    if quantidadeLitros <= 20:
        desconto = quantidadeLitros * 4
        valorLitroG = valorLitroG * quantidadeLitros
        valorTotal = valorLitroG - (valorLitroG * (desconto/100))
        
    elif quantidadeLitros > 20: 
        desconto = quantidadeLitros * 5
        valorLitroG = valorLitroG * quantidadeLitros
        valorTotal = valorLitroG - (valorLitroG * (desconto/100))

print(f'O valor total a ser pago é {valorTotal}')