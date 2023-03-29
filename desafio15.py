d = int(input('Informe a quantidade de dias:'))
km = float(input('Informe a quantidade de km rodados:'))
tp = (d * 60) + (km * 0.15)
print('O valor a se pagar para {} dias e {}km rodados é R${:.2F}' .format(d, km, tp))
