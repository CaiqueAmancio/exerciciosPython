"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
- o valor total a pagar com desconto de 10%;
- o valor de cada parcela, no parcelamento de 3x sem juros;
- a comissão do vendedor, no caso de venda a vista (5% sobre o valor com desconto)
- a comissão do vendedor, no caso de venda parcelada (5% sobre o valor total).
"""

valortotal = float(input(f'Olá, insira o valor total da compra: R$ '))
pagamentoavista = valortotal * 0.90
print(f'O valor total com desconto para pagamento a vista é: R$ {pagamentoavista}')
print(f'O valor de cada parcela, no caso de parcelamento em 3x sem juros: R$ {valortotal/3}')
print(f'O valor da comissão, no caso de venda a vista é: R$ {pagamentoavista * 0.05}')
print(f'O valor da comissão, no caso de venda parcelada é: R$ {valortotal * 0.05}')
