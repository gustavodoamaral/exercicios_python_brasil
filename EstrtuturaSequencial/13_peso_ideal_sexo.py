sexo = str(input('Informe seu sexo [M/F]: '))
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

if sexo == 'F':
    pesoIdeal = (62.1 * altura) - 44.7
else:
    pesoIdeal = (72.7 * altura) - 58

if peso > pesoIdeal:
    print(f'Você está acima do peso, seu peso ideal é: {pesoIdeal:.2f}')
if peso < pesoIdeal:
    print(f'Você está abaixo do peso, seu peso ideal é: {pesoIdeal:.2f}')
if peso == pesoIdeal:
    print(f'Você está no peso ideal, {pesoIdeal:.2f}')




