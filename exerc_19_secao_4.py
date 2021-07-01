"""
Leia um valor de volume em Litros e apresente-o convertido em metros cúbicos m³.
A fórmula de conversão é: M = L / 1000, sendo L o volume em litros e M em metro cúbico.
"""

volume = float(input(f'Digite um volume em litros e irei converter para metros cúbicos m³: '))
print(f'O volume em metros cúbicos m³ é: {volume / 1000}')
