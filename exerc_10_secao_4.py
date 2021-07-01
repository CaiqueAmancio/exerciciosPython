"""
Leia uma velocidade em km/h (quilômetro por hora) e apresente-a convertida em m/s (metros por segundo).
A fórmula de conversão é: M = K/3.6, sendo K a velolidade em km/h e M em M/s.
"""
velocidade = float(input(f'Olá, digite uma velocidade em Km/h e irei converter para M/s: '))
print(f'A velocidade é: {velocidade / 3.6} m/s')
