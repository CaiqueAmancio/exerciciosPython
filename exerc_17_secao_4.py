"""
Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C / 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.
"""

comprimento = float(input(f'Digite um comprimento em centímetros e irei converter para polegadas: '))
print(f'O comprimento em polegadas é: {comprimento / 2.54}')
