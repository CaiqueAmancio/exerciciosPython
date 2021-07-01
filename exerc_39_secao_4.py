"""
A importância de R$ 780 000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
- O primeiro irá receber 46%;
- O segundo irá receber 32%;
- O terceiro receberá o restante.
"""

valor = 780000
primeiro = valor * 0.46
segundo = valor * 0.32
terceiro = valor - (primeiro + segundo)

print(f'Um prêmio da loteria será divida entre três ganhadores.')
print(f'O valor do prêmio é: R$ {primeiro + segundo + terceiro} reais')
print(f'O primeiro irá receber: R$ {primeiro} reais')
print(f'O segundo irá receber: R$ {segundo} reais')
print(f'O terceiro irá receber: R$ {terceiro} reais')
