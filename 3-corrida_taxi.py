'''
Petrus, 09/03/2025
Modelo linear para cálculo de preço de corrida de taxi
'''

t=float(input("Digite o valor da tarifa: "))
d=float(input("Digite a distância percorrida em km: "))
b=float(input("Digite o valor da bndeirada: "))

def taxi(tarifa, distancia, bandeirada):
  return tarifa*distancia+bandeirada

print ('O valor total da corrida é R$', taxi(t, d, b))
