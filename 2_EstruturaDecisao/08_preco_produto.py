primeiroProduto = float(input('Informe o valor do primeiro produto: '))
segundoProduto = float(input('Informe o valor do segundo produto: '))
terceiroProduto = float(input('Informe o valor do terceiro produto: '))

if primeiroProduto == segundoProduto and primeiroProduto == terceiroProduto:
    print('O preço dos produtos são iguais')

elif primeiroProduto < segundoProduto and primeiroProduto < terceiroProduto:
    print('O primeiro produto é o mais barato. Você deve compra-lo')

elif segundoProduto < terceiroProduto:
    print('O segundo é o mais barato. Você deve compra-lo')

else:
    print('O terceiro é o mais barato. Você deve compra-lo')