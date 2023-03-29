# Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar.
# considere US$1,00= R$3,27
# ----------------------------------------------------------------------------------------------------------------------
print('Converta reais em dolares')
d = float(input('Quantos reais você tem disponível?'))
r = d
dr = d / 3.27
print('Com  R${: .2f}, você podera comprar US${: .2f}' .format(d, dr))
