#Escreva um programa que leia o nome, e o sobrenome,
# CONCATENE em uma nova variável nome completo, e retorne para o usuário



#Armazena os dados

nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))

Nome_completo = nome  + ' ' + sobrenome

#Armazena os dados
print(f'Seu nome completo é: {Nome_completo}')