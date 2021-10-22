populacaoA = 0 
while True: 
    populacaoA = int(input('Informe a população do país A: '))  
    if populacaoA < 0: 
        print('O valor da poupação deve ser positivo')
    else: 
        break 

crescimentoA = 0   
while True:   
    crescimentoA = float(input('Informe a taxa de crescimento da população do país A: '))
    if crescimentoA < 0: 
        print('O valor da taxa de crescimento precisa ser positivo')
    else: 
        break

populacaoB = 0 
while True: 
    populacaoB = int(input('Informe a população do país B: '))  
    if populacaoB < populacaoA: 
        print('O valor da poupação B deve ser maior que população A')
    else: 
        break 

crescimentoB = 0   
while True:   
    crescimentoB = float(input('Informe a taxa de crescimento da população do país B: '))
    if crescimentoB < 0: 
        print('O valor da taxa de crescimento precisa ser positivo')
    else: 
        break

anos = 0
while populacaoA < populacaoB: 
    populacaoA += populacaoA + (populacaoA * (crescimentoA/100))
    populacaoB += populacaoB + (populacaoB * (crescimentoB/100))
    anos += 1 
    if populacaoA == populacaoB: 
        anos -= 1
        break

print(f'Seram necessarios {anos} anos para o país A ultrapassar ou se igualar ao B em população\n'
      f'População do país A: {populacaoA}\n'
      f'População do país B: {populacaoB}')