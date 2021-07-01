"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
(a² + b²) ** (1/2) - raiz quadrada. Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
"""

print(f'Para realizar o cálculo da hipotenusa de um triângulo, insira os valores dos catetos a e b.')
catetoa = float(input(f'Insira o valor de a: '))
catetob = float(input(f'Insira o valor de b: '))
print(f'A hipotenusa é: {((catetoa ** 2) + (catetob ** 2)) ** (1/2)}')
