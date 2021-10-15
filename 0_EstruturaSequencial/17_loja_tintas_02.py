metrosQuadrados = float(input('Informe o tamanho em metros quadrados: '))

litros = (metrosQuadrados / 6.0) * 1.1   # 10% DE FOLGA
quantidadeLatas = int(litros / 18.0)
quantidadeGaloes = int(litros / 3.6)

if (litros % 18 != 0):
      quantidadeLatas += 1

if (litros % 3.6 != 0):
    quantidadeGaloes += 1

mixLatas = int(litros / 18.0)
mixGaloes = int((litros - (mixLatas * 18.0)) / 3.6)

if ((litros - (mixLatas * 18.0) % 3.6 != 0)):
    mixGaloes += 1

valorLatas = quantidadeLatas * 80.0
valorGaloes = quantidadeGaloes * 25
valorMix = (mixLatas * 80) + (mixGaloes * 25)


print(f'Quantidades de tinta a serem compradas e os respectivos preços em 3 situações:\n'
      f'Apenas latas de 18 litros: {quantidadeLatas} latas - R$ {valorLatas}\n'
      f'Apenas galões de 3,6 litros: {quantidadeGaloes} galões - R$ {valorGaloes}\n'
      f'Misturar latas e galões (desperdício menor): {quantidadeLatas} latas e {quantidadeGaloes} galões - R$ {valorMix}')