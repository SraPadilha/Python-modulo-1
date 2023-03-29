# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, Cosseno e tangente desse ângulo.
import math
angulo= int(input('Informe o angulo desejado:'))
seno= math.sin(angulo)
cosseno= math.cos(angulo)
tang= math.tan(angulo)
print('O ângulo {} tem como seu seno {:.2}, cosseno {:.2}, tangente {:.2}'.format(angulo, seno, cosseno, tang))

# resolução do professor:
import math
angulo= int(input('Informe o angulo desejado:'))
seno = math.sin(math.radians(angulo))
cosseno  = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O ângulo {} tem como seu seno {:.2f}, cosseno {:.2f}, tangente {:.2}'.format(angulo, seno, cosseno, tang))
