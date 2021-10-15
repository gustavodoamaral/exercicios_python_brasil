salarioAtual = float(input('Informe o salário atual: '))

if (salarioAtual <= 280):
    percentual = 20

elif (salarioAtual <= 700):
    percentual = 15

elif (salarioAtual <= 1500):
    percentual = 10

else:
    percentual = 5

aumento = salarioAtual * (percentual / 100.0)
novoSalario = salarioAtual + aumento

print(f'O salário antes do reajuste: {salarioAtual}')
print(f'O percentual de aumento aplicado: {percentual}%')
print(f'O valor de aumento: {aumento}')
print(f'Novo salário após aumento: {novoSalario}')