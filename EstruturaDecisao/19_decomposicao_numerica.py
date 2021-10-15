numero = int(input('Informe um número inteiro menor que 1000: '))

centenas = int(numero / 100)
unidades = int(numero % 10)
dezenas = int(((numero - unidades) / 10) % 10)

saidac = str
saidau = str
saidad = str

if centenas == 0 or centenas > 1:
    saidac = f"{centenas} centenas"
else: 
    saidac = f"{centenas} centena"


if dezenas == 0 or dezenas > 1:
    saidad = f"{dezenas} dezenas"
else: 
    saidad = f"{dezenas} dezena"


if unidades == 0 or unidades > 1:
    saidau = f"{unidades} unidades"
else: 
    saidau = f"{unidades} unidade"


print(f"{saidac}, {saidad} e {saidau}")