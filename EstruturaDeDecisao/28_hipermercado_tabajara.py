tipoCarne = str(input('Informe o tipo de carne desejado da promoção: \n[1]File Duplo \n[2]Alcatra \n[3]Picanha \n'))
quantidadeKg = int(input('Infome a quantidade em Kg: '))
formaPagamento = str(input('Formas de Pagamento: \n[1] Cartão Tabajara \n[2] Dinheiro \n[3] Pix \n[4] Outros Cartões \n'))

if quantidadeKg <= 5: 
    valorFileDuplo = 4.90 
    valorAlcatra = 5.90 
    valorPicanha = 6.90
else:
    valorFileDuplo = 5.80 
    valorAlcatra = 6.90 
    valorPicanha = 9.80

if tipoCarne == 'File Duplo': 
    valorTotal = valorFileDuplo * quantidadeKg
    if formaPagamento == 'Cartão Tabajara': 
        valorDesconto = valorTotal * 0.05
        valorPagar = valorTotal - valorDesconto
    else: 
        valorDesconto = 0 
        valorPagar = valorTotal

if tipoCarne == 'Alcatra': 
    valorTotal = valorAlcatra * quantidadeKg
    if formaPagamento == 'Cartão Tabajara': 
        valorDesconto = valorTotal * 0.05
        valorPagar = valorTotal - valorDesconto
    else: 
        valorDesconto = 0 
        valorPagar = valorTotal

if tipoCarne == 'Picanha': 
    valorTotal = valorPicanha * quantidadeKg
    if formaPagamento == 'Cartão Tabajara': 
        valorDesconto = valorTotal * 0.05
        valorPagar = valorTotal - valorDesconto
    else: 
        valorDesconto = 0 
        valorPagar = valorTotal

print(f'\nCUPOM FISCAL: \nTipo de Care: {tipoCarne} \nQuantidade: {quantidadeKg} kg. \nPreço Total: {valorTotal:.2f} \nForma de Pagamento: {formaPagamento} \nValor do Desconto: {valorDesconto:.2f} \nValor a Pagar: {valorPagar:.2f}')