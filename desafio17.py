# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.
import math
co= float(input('Digite o valor do cateto oposto:'))
ca= float(input('Digite o valor do cateto adjacente:'))
hi=math.hypot(co,ca)
print('A hipotenusa vai medir:{:.2f}' .format(hi))

# resolução do professor:
co = float( input('Digite o valor da cateto oporto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hi= (co** 2 + ca ** 2) **(1/2)
print(' um triangulo tendo {} como cateto oposto e {} como cateto adjacente, tera como hipotenusa '
      'aproximadamente {:.2f}'.format(co, ca, hi))

#ou
import math
co= float(input('Digite o valor do cateto oposto:'))
ca= float(input('Digite o valor do cateto adjacente:'))
hi=math.hypot(co,ca)
print('A hipotenusa vai medir:{:.2f}' .format(hi))
