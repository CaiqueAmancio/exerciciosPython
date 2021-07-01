"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
A fórmula de conversão é: k = C + 273.15, sendo C a temperatura em celsius
e K a temperatura em Kelvin.
"""
print("Olá, digite uma temperatura em Celsius que irei lhe mostrar a conversão para Kelvin.")
celsius = float(input(f'Digite a temperatura em Celsius: '))
print(f'A temperatura em Kelvin é: {celsius + 273.15}')
