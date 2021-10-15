kgMorangos = int(input('Informe a quantidade em quilos dos morangos: '))
kgMacas = int(input('Informe a quantidade em quilos das maças: '))

if kgMorangos <= 5:
    valorMorangos = 2.50
else: 
    valorMorangos = 2.20

valorTotalMorangos = valorMorangos * kgMorangos
 
if kgMacas <= 5:
    valorMacas = 1.80
else: 
    valorMacas = 1.50

valorTotalMacas = valorMacas * kgMacas

valorTotalFrutas = valorTotalMorangos + valorTotalMacas

if (kgMorangos + kgMacas) > 8 or valorTotalFrutas > 25:
    valorTotalFrutas = valorTotalFrutas - (valorTotalFrutas * 0.1)

print(f'Sua compra de frutas ficou no valor de: R$ {valorTotalFrutas}')

