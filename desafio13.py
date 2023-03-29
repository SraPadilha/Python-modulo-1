# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.
# ----------------------------------------------------------------------------------------------------------------------
print('Descubra qual será seu salário, em reais, com 15% de aumento ')
s = float(input('Digite seu salário R$:'))
p = int(input('Digite a porcentagem:'))
a = p / 100
vs = s * a
sf = vs + s
print('Aumento de {}%' .format(p))
print('A quantidade em reais do aumento:R${: .2f}' .format(vs))
print('O salário com aumento de {}%: R${: .2f}' .format(p, sf))
