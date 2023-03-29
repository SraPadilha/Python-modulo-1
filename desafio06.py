# Crie um algoritimo que leia um número e
# mostre o seu dobro, triplo e raiz quadrada.
# ----------------------------------------------------------------------------------------------------------------------
print('Descubra qual o dobro, o triplo, e a raiz quadrada de um número.')
n = float(input('Escolha um número e digite ele aqui: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('O dobro de {} é igual a {} e seu triplo {}!'.format(n, d, t))
print('e a raiz quadrada de {} é {: .2f}'.format(n, rq))

