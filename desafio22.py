#crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas.
# o nome com todas as letras minúsculas.xasjhd a
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
#-----------------------------------------------------------------------------------------------------------------------
# = input(str('Digite um nome: '))
#print (n.upper())
#print(n.lower())
#----------------------------------------------------------------------------------------------------------------------
#resolução do professor:

nome = str(input('Digite um nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome {} letras' .format(nome.find(' ')))
#ou
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras ao todo'.format(separa[0], len(separa[0])))