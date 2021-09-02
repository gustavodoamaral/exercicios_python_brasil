sexo = str(input('Informe seu sexo [M/F]: '))
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

if sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = (72.7 * altura) - 58

if peso > peso_ideal:
    print(f'Você está acima do peso, seu peso ideal é: {peso_ideal:.2f}')
if peso < peso_ideal:
    print(f'Você está abaixo do peso, seu peso ideal é: {peso_ideal:.2f}')
if peso == peso_ideal:
    print(f'Você está no peso ideal, {peso_ideal:.2f}')




