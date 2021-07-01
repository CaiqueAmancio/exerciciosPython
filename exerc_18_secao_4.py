"""
Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros.
A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M em metro cúbico.
"""

volume = float(input(f'Digite um volume em metros cúbicos e irei converter para litros: '))
print(f'O volume em litros é: {volume * 1000}')
