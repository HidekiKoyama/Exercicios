#Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário

#Armazena os dados
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade = input('Digite sua cidade: ')
nasc = str(input('Digite sua data de nascimento: '))

# Retorna as informaçõe para o usuário
print(f'Seu nome é {nome}, sua idade é {idade}, ' +
        f'voce mora em {cidade}, e nasceu em {nasc}')