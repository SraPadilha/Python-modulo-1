c = float(input('Digite a temperatura atual em ºC:'))
f = ((9* c) / 5) + 32
k = c + 273
print('A temperatura de {}ºC em Fahrenheit é {}ºF' .format(c, f))
print(' A temperatura de {}ºC em kelvin é {}k' .format(c, k))
tf= float( input('Digite a temperatura em ºF:'))
gc = (tf - 32) / 1.8
print('A temperatura {}ºF é {:.2f}ºC' .format(tf, gc))
