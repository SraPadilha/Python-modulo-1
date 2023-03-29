# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.
# resolução:
nome = input('olá, qual é o seu nome?')
print('Muito prazer {}!, vamos jogar algo inteligente?!'.format(nome))
print( 'O jogo segue as seguintes regras:')
print('1-Você nos informa alguma palavra, número ou simbolo.')
print('2-Depois iremos fazer uma afirmação sobre a informação digitada, abrindo espaço para uma resposta.')
print('3-O gabarito será mostrado logo abaixo com "true" para indicar uma afirmação verdadeira')
print( 'e "False" para uma afirmação falsa')
n = input('Digite algo:')
pergunta= input('O que foi digitado é um número')
print(n.isnumeric())
print('e seu type é')
print(type(n))

# Resolução do professor:
a = input('Digite algo:')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?',a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumério?', a.isalnum())
print('Está em maiúsculas?'), a.isupper()
print('Está em minúsculas?', a.islower())
print('Está capitalizada?'), a.istitle()
print(''), a.isascii()
