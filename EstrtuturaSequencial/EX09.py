#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

print('')

F = int(input('Temperature in Fahrenheit: '))

C = 5 * ((F-32)/9)

print(f'Its temperature in Celsius is: {C:.4f}')