print('Digite 1 para SIM ou 0 para NÃO')
try:
    pergunta1 = int(input("Telefonou para a vítima? \n[1] SIM \n[0] NÃO \n"))
    pergunta2 = int(input("Esteve no local do crime? \n[1] SIM \n[0] NÃO \n"))
    pergunta3 = int(input("Mora perto da vítima? \n[1] SIM \n[0] NÃO \n"))
    pergunta4 = int(input("Devia para a vítima? \n[1] SIM \n[0] NÃO \n"))
    pergunta5 = int(input("Já trabalhou com a vítima? \n[1] SIM \n[0] NÃO \n"))
except TypeError:
    print('Digite apenas "0" ou "1" para responder as perguntas')

pontos = pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5

if pontos == 2: 
    classificacao = 'Suspeito'
elif pontos >= 3 and pontos <= 4:
    classificacao = 'Cumplice'
elif pontos == 5: 
    classificacao = 'Assassino'
else: 
    classificacao = 'Inocente'

print(classificacao)