#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = int(input('Descubra a área de um circulo a partir de seu raio.\nDigite o raio: '))

pi = 3.14

area = (pi * raio) ** 2 

print(f'A área do circulo é de: {round(area)}')