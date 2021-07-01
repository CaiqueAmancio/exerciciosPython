"""
leia um número inteiro e imprima a soma do sucessor de seu triplo com
antecessor de seu dobro.
"""

num = int(input(f'Digite um número inteiro e irei mostrar a soma do sucessor de seu triplo com '
                f'antecessor de seu dobro: '))
triplo = (num * 3) + 1
dobro = (num * 2) - 1
print(f'A soma do sucessor de seu triplo com o antecessor de'
      f' seu dobro é: {triplo + dobro }')
