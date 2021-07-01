"""
Faça um programa para ler o valor do raio de um círculo, e depois mostrar o valor da área deste círculo com quatro
casas decimais conforme exemplos.
Fórmula: area = pi * raio²
considere o valor de pi = 3.14159
Entrada = 2.00 ; Saída = A = 12.5664
"""

raio = float(input('Digite o raio de um círculo: '))

area = 3.14159 * (raio ** 2)

print(f'A área do círculo é: {area:.4f}')
