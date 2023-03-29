# Faça um programa que leia a largura em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2.
# ----------------------------------------------------------------------------------------------------------------------
print('Descubra a área e a quantidade, em litros de tinta, necessaria para pintar uma parede')
lp = float(input('Digite a largura da parede em metros:'))
ap = float(input('Digite a altura da parde em metros:'))
a = lp * ap
qt = a / 2
print('Área da parede: {}m²' .format(a))
print('Quandidade de tinta para pintá-la: {: .2f} Litros de tinta.' .format(qt))
