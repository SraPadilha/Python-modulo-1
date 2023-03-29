# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# inteiro para menos:
import math
print('Para arredondar para menos-')
n = float(input('Digite um número qualquer:'))
r = math.floor(n)
print(' O número {} tem como seu inteiro {}'.format(n, r))
#inteiro para mais:
print ('Para arredondar para mais-')
import math
n = float(input('Digite um número qualquer:'))
r = math.ceil(n)
print(' O número {} tem como seu inteiro {}'.format(n, r))
# versão do professor:
import math
n = float(input('Digite um número qualquer:'))
print(' O número {} tem como seu inteiro {}'.format(n, math.trunc(n)))
# ou
from math import trunc
n = float(input('Digite um número qualquer:'))
print(' O número {} tem como seu inteiro {}'.format(n, trunc(n)))
