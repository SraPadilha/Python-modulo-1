# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
# ----------------------------------------------------------------------------------------------------------------------
p = float(input('Preço original do produto: R$'))
d = 5 / 100
vf = p * d
r = p - vf
print('Deconto de 5%')
print('Valor final do produto: R${: .2f}' .format(r))

