"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * (9.0/ 5.0) +32.0 , sendo C a temperatura em celsius
e F a temperatura em Fahrenheit.
"""

print("Olá, digite uma temperatura em Celsius que irei lhe mostrar a conversão para Fahrenheit.")
celsius = float(input(f'Digite a temperatura em Celsius: '))
print(f'A temperatura em Fahrenheit é: {celsius * (9.0 / 5.0) + 32.0}')
