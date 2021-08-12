#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

cont = 1
aux = 0 

while cont != 5: 
    nota = float(input(f'Digite a {cont} nota: '))
    aux += nota
    cont += 1 

media = aux / 4 

print(f'A média é {media}')