"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = k - 273.15, sendo C a temperatura em celsius
e K a temperatura em Kelvin.
"""
print("Olá, digite uma temperatura em Kelvin que irei lhe mostrar a conversão para Celsius.")
kelvin = float(input(f'Digite a temperatura em Kelvin: '))
print(f'A temperatura em Celsius é: {kelvin - 273.15}')
