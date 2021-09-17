cont = 1
auxiliar = 0

while cont != 5: 
    nota = float(input(f'Digite a {cont} nota: '))
    auxiliar += nota
    cont += 1 

media = auxiliar / 4

print(f'A média é {media}')