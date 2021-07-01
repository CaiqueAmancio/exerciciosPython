"""
Leia um ângulo em radiano e apresente-o convertido em graus. A fórmula de
conversão é : G = R * 180/Pi, sendo G o ângulo em graus, R em radianos e PI = 3,14.
"""

angulo = float(input(f'Digite um ângulo em radianos e irei converter para graus: '))
print(f'O ângulo em graus é: {angulo * (180 / 3.14)}')
