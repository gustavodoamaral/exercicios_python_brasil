numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))

operacao = str(input('\nEscolha uma operação aritmética! \n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Divisão \nQual operação você deseja realizar: ')).upper()

resultado = 0
if operacao == '1': 
    resultado = numero1 + numero2

elif operacao == '2': 
    resultado = numero1 - numero2

elif operacao == '3': 
    resultado = numero1 * numero2 

elif operacao == '4': 
    resultado = numero1 / numero2

else: 
    print('Escolha uma das 4 opções disponíveis! ;)')

if round(resultado) == resultado: 
    if int(resultado) % 2 == 0: 
        imparPar = 'Par'
    else:
        imparPar = 'Impar'
else: 
    imparPar = 'Apenas números inteiros podem ser classificados em "Impar ou Par"' 

if resultado > 0: 
    positivoNegativo = 'Positivo'
elif resultado < 0: 
    positivoNegativo = 'Negativo'
else: 
    positivoNegativo = 'Neutro'

if round(resultado) == resultado: 
    inteiroDecimal = 'Inteiro'
else: 
    inteiroDecimal = 'Decimal'

print(f'\nO resultado da operação aritimética {operacao} é: {resultado}\n \nImpar ou Par: {imparPar} \nPositivo ou Negativo: {positivoNegativo} \nInteiro ou Decimal: {inteiroDecimal}')