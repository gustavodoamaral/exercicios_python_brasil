# 1 litro == 3 metros quadrados
# tinta vendida em latas de 18 litros
# valor de cada lata: 80 reais

metrosQuadrados = float(input('Informe o tamanho em metros quadrados: '))

litros = metrosQuadrados / 3.0
quantidadeLatas = int(litros / 18.0)

if (litros % 18 != 0):
      quantidadeLatas += 1

valorTotal = quantidadeLatas * 80.0


print(f'Você deve comprar {quantidadeLatas} latas de tinta para {metrosQuadrados} metros quadrados.\n'
      f'Valor total: {valorTotal}')

