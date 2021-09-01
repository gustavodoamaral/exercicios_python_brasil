#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

C = int(input('Degrees in Celsius: '))

F = (C*1.8) + 32

print(f'Converted to Fahrenheit are: {F:.2f}')