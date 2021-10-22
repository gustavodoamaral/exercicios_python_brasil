populacaoA = 80000
populacaoB = 200000
anos = 0

while populacaoA < populacaoB: 
    populacaoA += populacaoA + (populacaoA * 0.03)
    populacaoB += populacaoB + (populacaoB * 0.015)
    anos += 1 
    if populacaoA == populacaoB: 
        anos -= 1
        break

print(f'Seram necessarios {anos} anos para o país A ultrapassar ou se igualar ao B em população\n'
      f'População do país A: {populacaoA}\n'
      f'População do país B: {populacaoB}')