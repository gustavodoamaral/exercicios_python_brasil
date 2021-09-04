peso_de_peixes = float(input("Informe os quilos: "))

excesso = peso_de_peixes - 50

multa = int(excesso) * 4

print(f'Você possui {peso_de_peixes}: Kg. de peixes '
      f'\nForam excedidos: {excesso} Kg. '
      f'\nO valor da multa é: {multa} (R$ 4,00 por Kg excedente.)')

