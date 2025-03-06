'''
Petrus, 06/03/2025
Função recursiva para calcular o fatorial de um número.
'''

numero = int(input("Digite um número para calcular seu fatorial: "))

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(numero))
