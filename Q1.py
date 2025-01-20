''' Q1. Troque o número sem usar a terceira variável.'''

x=int(input("Digite o primeiro número: "))
y=int(input("Digite o segundo número: "))
print(x,y)
x, y = y, x
print(x,y)
