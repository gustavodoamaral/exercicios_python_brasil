pesoPeixes = float(input("Informe os quilos: "))

excesso = pesoPeixes - 50

multa = int(excesso) * 4

print(f'Você possui {pesoPeixes}: Kg. de peixes '
      f'\nForam excedidos: {excesso} Kg. '
      f'\nO valor da multa é: {multa} (R$ 4,00 por Kg excedente.)')

