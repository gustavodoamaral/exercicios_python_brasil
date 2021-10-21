populacaoA = 80000
populacaoB = 200000

while populacaoA < populacaoB: 
    populacaoA += populacaoA + (populacaoA * 0.03)
    populacaoB += populacaoB + (populacaoB * 0.015)
    if populacaoA == populacaoB: 
        break

print(f'População do país A: {populacaoA}\n'
      f'População do país B: {populacaoB}')