while True: 
    nota = int(input('Informe uma nota entre 0 e 10: '))

    if nota >= 0 and nota <= 10: 
        break
    else: 
        print('Informe um valor válido')
        
print('Parabéns! Você informou o nota corretamente')