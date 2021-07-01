"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.
"""

comprimento = float(input(f'Digite um comprimento em polegadas e irei converter para centímetros: '))
print(f'O comprimento em centímetros é: {comprimento * 2.54}')
