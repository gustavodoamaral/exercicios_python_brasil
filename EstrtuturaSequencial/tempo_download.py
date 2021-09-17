tamanho = float(input('Informe o tamanho do arquivo (em MB): '))
velocidade = float(input('Informe a velocidade de conexao (em Mbps): '))

tempoSegundos = tamanho / (velocidade / 8)
tempoMinutos = tempoSegundos / 60

print(f'Tempo aproximado de download: {tempoMinutos} minutos')