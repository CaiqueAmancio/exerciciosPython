"""
Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é:
K = 1.61 * M, sendo K a distância em quilômetros e M em milhas.
"""

distancia = float(input(f'Digite uma distância em milhas e irei converter para quilômetros: '))
print(f'A distância em quilômetros é: { 1.61 * distancia}')
