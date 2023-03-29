# Faça um programa que leia um número inteiro
# e mostre na tela o seu sucessor e o seu antecessor.
# ex.: 8 é um número inteiro, o seu sucessor é o 9 e o seu antecessor o 7.
# ------------------------------------------------------------------------------------------------------------------------
n1 = int(input('Digite um número para ver o seu sucessor e o seu antecessor:'))
s = n1 + 1
a = n1 - 1
print('O sucessor de {} é {}, e o seu antecessor é {}'.format(n1, s, a))
