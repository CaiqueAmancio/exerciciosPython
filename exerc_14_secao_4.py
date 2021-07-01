"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de
conversão é : R = G * PI/180, sendo G o ângulo em graus, R em radianos e PI = 3,14.
"""

angulo = float(input(f'Digite um ângulo em graus e irei converter para radianos: '))
print(f'O ângulo em radianos é: {angulo * (3.14 / 180)}')
