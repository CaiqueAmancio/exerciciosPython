"""
Fazer um programa para ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o
código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Calcule e mostre o valor a ser pago
Exs de entradas: 12 1 5.30 ; 16 2 5.10
Exs de Saída: VALOR A PAGAR: R$ 15.50
"""

codigo_peca1 = float(input('\nDigite o código da peça 1: '))
numero_peca1 = float(input('\nDigite o número de peças 1: '))
valor_peca1 = float(input('\nDigite o valor unitário de cada peça 1: '))

peca1 = float(numero_peca1 * valor_peca1)

codigo_peca2 = float(input('\nDigite o código da peça 2: '))
numero_peca2 = float(input('\nDigite o número de peças 2: '))
valor_peca2 = float(input('\nDigite o valor unitário de cada peça 2: '))

peca2 = float(numero_peca2 * valor_peca2)

print(f'O valor a pagar é R$ {(peca1 + peca2):.2f} reais')
