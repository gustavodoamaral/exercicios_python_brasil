primeiraNota = float(input('Informe a primeira nota: '))
segundaNota = float(input('Informe a segunda nota: '))

media = (primeiraNota + segundaNota) / 2

if 9 <= media <= 10:
    conceito = 'A'
    situacao = 'APROVADO'

elif 7.5 <= media <= 9:
    conceito = 'B'
    situacao = 'APROVADO'

elif 6 <= media <= 7.5:
    conceito = 'C'
    situacao = 'APROVADO'

elif 4 <= media <= 6:
    conceito = 'D'
    situacao = 'REPROVADO'

elif 0 <= media < 4:
    conceito = 'E'
    situacao = 'REPROVADO'

else:
    media = 'Inválida'
    conceito = 'Inválida'
    situacao = 'Inválida'
    print('Informe notas válidas para visualizar média, conceito e situação')

print(f'1º nota: {primeiraNota} - 2º nota: {segundaNota}\n'
      f'Média: {media} - Conceito: {conceito} - Situação: {situacao}')
