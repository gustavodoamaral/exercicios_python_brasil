usuario = senha = 0

while usuario == senha:
    usuario = str(input('Informe o nome de usuário: '))
    senha = str(input('Informe a senha: '))
    if usuario == senha: 
        print('A senha não pode ser igual ao usuário')
    else: 
        print('Usuário autenticado')
