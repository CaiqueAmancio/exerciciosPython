"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0 * (F - 32.0) / 9.0, sendo C a temperatura em celsius
e F a temperatura em Fahrenheit.
"""
print("Olá, digite uma temperatura em Fahrenheit que irei lhe mostrar a conversão para Celsius.")
fahrenheit = float(input(f'Digite a temperatura em Fahrenheit: '))
print(f'A temperatura em Celsius é: {5.0 * (fahrenheit - 32.0) / 9.0}')
