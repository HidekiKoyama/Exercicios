#Escreva um programa que leia um tipo de dado e usando a função type(),
# retorne ao usuário, qual o tipo de dado informado

#Armazena os dados
texto = input('Digite seu dado: ')

tipo_de_dado = type(texto)

# Retorna as informaçõe para o usuário
print(f'O tipo do seu dado e: {tipo_de_dado}')