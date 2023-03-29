# Desenvolva um programa que leia as duas notas de um
# aluno, calcule e mostre a sua média.
# ----------------------------------------------------------------------------------------------------------------------
print('Calcule a média bismestral:')
p1 = float(input('Primeira prova:'))
p2 = float(input('Segunda prova:'))
s = p1 + p2
m = s / 2
print('Soma das notas:{: .1f}' .format(s))
print('Média:{: .1f}'.format(m))
print('--------------------------------------------------------------------------------------------------------------')
print('Explicação: Somando p1= {} e p2= {} (p1 + p2), obtemos o resultado= {: .1f}'.format(p1, p2, s))
print('O resultado da soma das notas do 1° bimestre é divido por 2 (que é quantidade de provas) \n e teremos a média.')
print('Logo, a média do 1º bimetre será= {: .1f}' .format(m))

